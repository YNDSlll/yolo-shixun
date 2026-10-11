import streamlit as st
import time
from ultralytics import YOLO
import os
from pathlib import Path

# ===================== 0. 路径与模型配置 =====================
# 以脚本所在目录为基准定位资源，避免云端运行时工作目录不同导致找不到文件
BASE_DIR = Path(__file__).resolve().parent

# 交通标志模型路径（4 类：prohibitory / danger / mandatory / other）
TRAFFIC_SIGNAL_MODEL_PATH = BASE_DIR / "runs/detect/trains/train-TrafficSignal/weights/best.pt"
# 人脸表情模型路径（8 类：Anger / Contempt / Disgust / Fear / Happy / Neutral / Sad / Surprise）
FACIAL_EXPRESSION_MODEL_PATH = BASE_DIR / "runs/detect/trains/train-FacialExpression/weights/best.pt"
# 若训练权重不可用时，可临时改用官方预训练权重做流程验证
# TRAFFIC_SIGNAL_MODEL_PATH = BASE_DIR / "yolo26n.pt"

# 上传图片与检测结果的存放目录
UPLOAD_PATH = BASE_DIR / "images/upload"
RESULT_PATH = BASE_DIR / "images/result"


@st.cache_resource(show_spinner=False)
def load_model(model_path: str) -> YOLO:
    """加载模型并缓存，同一进程内只加载一次，避免每次点击都重新载入权重"""
    return YOLO(model_path)


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
                    os.makedirs(UPLOAD_PATH, exist_ok=True)
                    os.makedirs(RESULT_PATH, exist_ok=True)
                    # 交通标志模型路径
                    model_path = TRAFFIC_SIGNAL_MODEL_PATH
                    status.info("开始加载交通标志检测模型")
                    if not model_path.exists():
                        status.update(label="模型文件缺失", state="error")
                        st.error(f"未找到模型权重：{model_path.name}\n\n请确认权重文件已随仓库一起上传（路径：runs/detect/trains/train-TrafficSignal/weights/best.pt）。")
                        st.stop()
                    upload_full_path = UPLOAD_PATH / filename
                    with open(upload_full_path, "wb") as f:
                        f.write(file_uploader.read())
                    status.success("成功存储待检测图片")
                    model = load_model(str(model_path))
                    status.success("成功加载模型")
                    status.info("开始执行检测...")
                    results = model.predict(source=str(upload_full_path), save=False)
                    status.success("检测完成")
                    result_save_path = RESULT_PATH / filename
                    results[0].save(str(result_save_path))
                    status.success("成功存储检测结果图片")
                    with col2:
                        st.subheader("检测结果")
                        st.image(image=str(result_save_path))

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
                    os.makedirs(UPLOAD_PATH, exist_ok=True)
                    os.makedirs(RESULT_PATH, exist_ok=True)
                    # 人脸表情模型路径
                    model_path = FACIAL_EXPRESSION_MODEL_PATH
                    # 如果还没训练好，先用预训练模型测试：
                    # model_path = BASE_DIR / "yolo26n.pt"
                    status.info("开始加载人脸表情检测模型")
                    if not model_path.exists():
                        status.update(label="模型文件缺失", state="error")
                        st.error(f"未找到模型权重：{model_path.name}\n\n请确认权重文件已随仓库一起上传（路径：runs/detect/trains/train-FacialExpression/weights/best.pt）。")
                        st.stop()
                    upload_full_path = UPLOAD_PATH / filename
                    with open(upload_full_path, "wb") as f:
                        f.write(file_uploader.read())
                    status.success("成功存储待检测图片")
                    model = load_model(str(model_path))
                    status.success("成功加载模型")
                    status.info("开始执行检测...")
                    results = model.predict(source=str(upload_full_path), save=False)
                    status.success("检测完成")
                    result_save_path = RESULT_PATH / filename
                    results[0].save(str(result_save_path))
                    status.success("成功存储检测结果图片")
                    with col2:
                        st.subheader("检测结果")
                        st.image(image=str(result_save_path))

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
