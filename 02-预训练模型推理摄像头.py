# 1.导入YOLO
from ultralytics import YOLO

if __name__ == '__main__':
    # 2.创建模型对象 (改回相对路径)
    model = YOLO("yolo26n.pt")
    
    # 3.设置推理资源为摄像头
    # 【避坑指南】在 Mac 上，0 通常是自带的 FaceTime 摄像头。
    # 但如果你旁边放着你的 iPhone 并开启了“连续互通”，Mac 可能会把 iPhone 识别为 0 摄像头。
    # 如果运行后发现没画面或者报错，把这里的 0 改成 1 即可。
    source = 0 
    
    print("📷 正在唤醒摄像头... ")
    print("⚠️  提示：请在弹出的视频画面中按下英文小写字母 'q' 键来安全退出！")
    
    # 4.调用predict方法执行推理
    # 【关键优化】
    # device='mps': 激活 M4 芯片加速，保证视频检测帧率更高，不卡顿。
    # save=False: 实时视频没必要一帧帧存下来，不然硬盘很快就满了。
    results = model.predict(source=source, save=False, device='cpu', show=True)
    
    print("✅ 摄像头已关闭，程序安全退出。")#按字母q退出后会执行到这里，提示用户程序已安全退出。
