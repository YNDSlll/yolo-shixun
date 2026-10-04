from ultralytics import YOLO

if __name__ == '__main__':
    # ================= 第一阶段：模型推理 =================
    
    # 1. 加载预训练模型
    model = YOLO("yolo26n.pt")
    
    # 2. 设置要检测的图片路径 (请确保路径下有这张图片)
    source = "ultralytics/assets/bus.jpg"
    
    # 3. 执行推理命令
    # device='mps'：启用专属硬件加速，提升处理速度
    # save=False：关闭默认保存机制，由我们用代码来掌控结果
    results = model.predict(source=source, save=False, device='cpu')
    
    # ================= 第二阶段：数据解析 =================
    
    # 4. 提取单张图片的结果
    # 因为我们只传入了一张图片，所以直接取出 results 列表中的第 0 个元素
    result = results[0]
    
    # 获取这张图片里被 AI 圈出来的所有目标的集合 (boxes)
    boxes = result.boxes
    
    print(f"\n✅ 图片扫描完成！AI 在这张图里一共发现了 {len(boxes)} 个目标。\n")
    print("=" * 40)
    
    # 5. 遍历并“解剖”每一个被检测到的目标
    for index, box in enumerate(boxes):
        
        # --- 提取类别信息 ---
        # .item() 将 Tensor 格式转换为普通数字
        cls_index = int(box.cls.item()) 
        # 去模型的字典里查阅这个数字对应的英文单词
        class_name = result.names[cls_index]
        
        # --- 提取置信度 (AI 有多自信) ---
        # 提取出来后保留 2 位小数，看起来更直观
        conf = round(box.conf.item(), 2)
        
        # --- 提取位置坐标 ---
        # .tolist() 将 Tensor 格式转换为 Python 列表
        # 依次解包赋值给 左上角(x_min, y_min) 和 右下角(x_max, y_max)
        x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
        
        # 打印展示这个目标的详细档案
        print(f"📦 目标序号 {index + 1}:")
        print(f"  ▶ 识别类别 : {class_name}")
        print(f"  ▶ 确 定 性 : {conf * 100}%") # 乘以100换算成百分比更好理解
        print(f"  ▶ 坐标位置 : 左上角({int(x_min)}, {int(y_min)}), 右下角({int(x_max)}, {int(y_max)})")
        print("-" * 40)

    # (可选) 网页开发铺垫：如果后续需要将画好框的图片传给网页，可以使用这段代码保存
    result.save("web_output.jpg")