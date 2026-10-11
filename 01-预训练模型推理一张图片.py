# 1.导入YOLO
from ultralytics import YOLO

if __name__ == '__main__':
    # 2.创建模型对象
    # yolo26n.pt 是官方 COCO 预训练权重，未随仓库发布，首次运行会自动下载到项目根目录
    model = YOLO("yolo26n.pt")

    # 3.设置图片路径（和你的项目结构一致）
    source = "ultralytics/assets/bus.jpg"

    # 4. 直接推理并保存到当前项目目录
    results = model.predict(
        source=source,
        save=True,
        device='cpu',
        project="./",          # 保存的根目录，设置为当前项目根目录
        name="runs",           # 保存的子文件夹名
        exist_ok=True          # 允许覆盖已存在的文件夹
    )