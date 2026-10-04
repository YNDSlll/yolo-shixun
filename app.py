import streamlit as st
import time
from ultralytics import YOLO
import os

# ===================== 1. 初始化会话状态 =====================
if "is_login" not in st.session_state:
    st.session_state.is_login = False
if "login_username" not in st.session_state:
    st.session_state.login_username = None
if "current_page" not in st.session_state:
    st.session_state.current_page = "home_page"

# ===================== 2. 登录页面 =====================
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("欢迎登陆")
        with st.form("login_form"):
            username = st.text_input(label="账号", placeholder="输入账号", key="username")
            password = st.text_input(label="密码", placeholder="请输入密码", type="password", key="password")
            submit_button = st.form_submit_button(label="登陆", width="stretch")
            if submit_button:
                if username != "lhy":
                    msg = st.error("账号错误")
                    time.sleep(2)
                    msg.empty()
                elif password != "111":
                    msg = st.error("密码错误")
                    time.sleep(2)
                    msg.empty()
                else:
                    msg = st.success("登陆成功")
                    st.session_state.is_login = True
                    st.session_state.login_username = username
                    time.sleep(2)
                    msg.empty()
                    st.rerun()

# ===================== 3. 系统首页 =====================
def home_page():
    st.title("欢迎使用我的目标检测系统")
    st.write("这是一个基于YOLO的多目标检测网页应用")
    st.write("请从左侧菜单栏选择功能：")
    st.markdown("- 交通标志检测：识别禁止、危险、强制等交通标志")
    st.markdown("- 人脸表情检测：识别生气、开心、惊讶等8种表情")

# ===================== 4. 交通标志检测页面 =====================
def traffic_signal_detection_page():
    st.title("🚦 交通标志检测系统")
    file_uploader = st.file_uploader(label="请选择检测图片", type=["jpg", "jpeg", "png"])
    if file_uploader is not None:
        col1, col2 = st.columns([1,1])
        with col1:
            st.subheader("待检测图片")
            st.image(image=file_uploader)
            if st.button(label="开始检测", type="primary"):
                with st.status("准备开始执行检测任务...", expanded=True) as status:
                    filename = str(int(time.time())) + ".jpg"
                    upload_path = "images/upload"
                    result_path = "images/result"
                    os.makedirs(upload_path, exist_ok=True)
                    os.makedirs(result_path, exist_ok=True)
                    # 交通标志模型路径
                    model_path = "./runs/detect/trains/train-TrafficSignal/weights/best.pt"
                    upload_full_path = os.path.join(upload_path, filename)
                    with open(upload_full_path, "wb") as f:
                        f.write(file_uploader.read())
                    status.success("成功存储待检测图片")
                    status.info("开始加载交通标志检测模型")
                    model = YOLO(model_path)
                    status.success("成功加载模型")
                    status.info("开始执行检测...")
                    results = model.predict(source=upload_full_path, save=False)
                    status.success("检测完成")
                    result_save_path = os.path.join(result_path, filename)
                    results[0].save(result_save_path)
                    status.success("成功存储检测结果图片")
                    with col2:
                        st.subheader("检测结果")
                        st.image(image=result_save_path)

# ===================== 5. 人脸表情检测页面 =====================
def facial_expression_detection_page():
    st.title("😊 人脸表情检测系统")
    file_uploader = st.file_uploader(label="请选择检测图片", type=["jpg", "jpeg", "png"])
    if file_uploader is not None:
        col1, col2 = st.columns([1,1])
        with col1:
            st.subheader("待检测图片")
            st.image(image=file_uploader)
            if st.button(label="开始检测", type="primary"):
                with st.status("准备开始执行检测任务...", expanded=True) as status:
                    filename = str(int(time.time())) + ".jpg"
                    upload_path = "images/upload"
                    result_path = "images/result"
                    os.makedirs(upload_path, exist_ok=True)
                    os.makedirs(result_path, exist_ok=True)
                    # 人脸表情模型路径
                    model_path = "./runs/detect/trains/train-FacialExpression/weights/best.pt"
                    # 如果还没训练好，先用预训练模型测试：
                    # model_path = "yolo26n.pt"
                    upload_full_path = os.path.join(upload_path, filename)
                    with open(upload_full_path, "wb") as f:
                        f.write(file_uploader.read())
                    status.success("成功存储待检测图片")
                    status.info("开始加载人脸表情检测模型")
                    model = YOLO(model_path)
                    status.success("成功加载模型")
                    status.info("开始执行检测...")
                    results = model.predict(source=upload_full_path, save=False)
                    status.success("检测完成")
                    result_save_path = os.path.join(result_path, filename)
                    results[0].save(result_save_path)
                    status.success("成功存储检测结果图片")
                    with col2:
                        st.subheader("检测结果")
                        st.image(image=result_save_path)

# ===================== 6. 主页面布局（侧边栏+页面切换） =====================
def index_page():
    with st.sidebar:
        st.title("目标检测系统")
        st.write(f"欢迎 {st.session_state.login_username} 使用")
        with st.expander("系统管理"):
            if st.button("系统首页", key="home_page", width="stretch"):
                st.session_state.current_page = "home_page"
                st.rerun()
        with st.expander("交通标志检测"):
            if st.button("图片检测", key="traffic_signal_detection_page", width="stretch"):
                st.session_state.current_page = "traffic_signal_detection_page"
                st.rerun()
        with st.expander("人脸表情检测"):
            if st.button("图片检测", key="facial_expression_detection_page", width="stretch"):
                st.session_state.current_page = "facial_expression_detection_page"
                st.rerun()
    # 页面映射字典
    page_functions = {
        "home_page": home_page,
        "traffic_signal_detection_page": traffic_signal_detection_page,
        "facial_expression_detection_page": facial_expression_detection_page
    }
    if st.session_state.current_page in page_functions:
        page_functions[st.session_state.current_page]()

# ===================== 7. 主逻辑 =====================
if not st.session_state.is_login:
    login_page()
else:
    index_page()