from ultralytics import YOLO, YOLOv10

model_name = "LK_YOLOv10_cfg.yaml"

# 加载模型。
if "v10" in model_name:
    model = YOLOv10(model_name)  # 如果你要加载v10模型请用这个类。
else:
    model = YOLO(model_name)  # 如果你要加载其他模型就用这个类。

# 训练模型，具体参数需要在配置文件里面修改。
# 请你为每种模型额外修改一个名字，不要使用default.yaml
model = model.train(cfg="LK_YOLOv10_cfg.yaml", data="manhole.yaml")

# test