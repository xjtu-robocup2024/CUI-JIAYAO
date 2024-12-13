import mouse
from ultralytics import YOLO
import keyboard
import os
import time
# 加载训练好的模型，改为自己的路径
model = YOLO(r"C:\Users\ASUS\Desktop\ultralytics-8.3.30\trained_yolov8n.pt")

# 无限循环，直到按下ESC键
while True:

    # 修改为自己的图像或者文件夹的路径（这里可以设置为None来测试重新执行循环的功能）
    source = r"C:\Users\ASUS\Desktop\video\latest_screen_capture.png" # 或者设置为 None 来模拟无效路径

    # 检查图像路径是否为None或文件是否存在
    if source is None or not os.path.isfile(source):
        print("图像路径无效或文件不存在，重新执行循环。")
        continue  # 跳过当前循环的剩余部分，并重新开始循环

    try:
        # 运行推理，并附加参数
        results = model.predict(source, save=True, show=False, conf=0.9)

        # 检查模型是否返回了结果
        if results:

            # 注意：这里假设results是一个列表，每个元素都是一个包含检测结果的对象
            #这里应该加一个延时操作，如果检测到目标后进行间断点击
            for detection in results:
                # 获取边界框列表（注意：这里假设每个检测结果都有一个boxes属性）
                boxes = detection.boxes
                # 检查边界框列表是否为空
                if boxes:
                    # 获取第一个边界框（注意：这里假设boxes是一个列表，且每个元素都是一个边界框对象）
                    box = boxes[0]
                    # 获取边界框的数据（注意：这里假设box.data是一个有效的属性，并且您知道它的结构）
                    box_data = box.data  # 假设box.data是一个包含坐标的列表或数组

                    # 计算边界框的中心点
                    x = (box_data[0][0] + box_data[0][2]) / 2
                    y =  box_data[0][1]+5

                    # 移动鼠标到边界框的中心点
                    mouse.move(int(x/1.5), int(y/1.5))
                    mouse.click('left')
                    mouse.click('left')

                    time.sleep(1)
                    # 打印边界框的数据（可选）
                    print(box_data)

                else:
                    print("未检测到任何边界框。")
        else:
            print("模型未返回任何结果。")

    except Exception as e:
        # 捕获并打印任何异常，然后重新执行循环
        print(f"发生错误：{e}。重新执行循环。")

    # 检查是否按下了ESC键
    if keyboard.is_pressed('esc'):
        print("ESC键已按下。停止程序...")
        break  # 退出循环