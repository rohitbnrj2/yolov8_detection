from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

# Use the model
model.train(data="config.yaml", epochs=100)  # train the model
metrics = model.val()  # evaluate model performance on the validation set

test_imgs = ['test01.jpg', 'test02.jpg']

for i in range(len(test_imgs)):
    results = model(test_imgs[i])  # predict on an image

path = model.export(format="onnx")  # export the model to ONNX format