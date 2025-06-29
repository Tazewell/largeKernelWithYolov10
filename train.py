from ultralytics import YOLO, YOLOv10

model_name = "LK_YOLOv10_cfg.yaml"

# 加载模型。
if "v10" in model_name:
    model = YOLOv10(model_name) 
else:
    model = YOLO(model_name) 

# 训练模型，具体参数需要在配置文件里面修改。

model = model.train(cfg="LK_YOLOv10_cfg.yaml", data="manhole.yaml")

# test