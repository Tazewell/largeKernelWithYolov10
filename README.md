# README

项目运行的依赖在根目录下的requirements.txt里面，如果要导入依赖的话，在根目录下打开命令行，激活环境，可以执行

```
pip install -r requirements.txt
```

即可运行项目

## ultralytics

### cfg
这里面存储着各个配置文件。

请注意，cfg中有一个配置文件叫做default.yaml，里面集成了训练选项和训练参数，如果要重新训练的话请注意里面的描述。
#### datasets
这里面存储着数据集配置文件。

格式可以按照ImageNet.yaml进行修改。如果要在训练中调用，请确保配置文件在这个文件夹里。
#### models
存储着模型配置文件。

我们的模型在下面的v10文件夹里，名字叫LK_YOLOv10。
### nn
存储着项目的模块设计，在modules/block.py中，你可以看见我们的RepLKBlock模块。

# 训练

如果要训练，请你使用项目里的train.py，在其基础上修改训练，训练后的结果会保存在runs文件夹下。# largeKernelWithYolov10
