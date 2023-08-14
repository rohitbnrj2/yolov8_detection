<H2> YOLO Object Detection Using Custom Dataset </H2>

This is a simple project where by using YOLOv8 a custom dataset is classified based on the object of interest. The following have been completed - 
1. Successfully ran the basic yolo predict and train based on the instructions provided in the ultralytics README.md.
2. Used different yaml files to test against different datasets, such as VisDrone, COCO and OpenImagesV7.
3. Built a custom dataset using [makesense.ai](https://www.makesense.ai/) and downloaded the images from google.
4. Wrote a python script based on instructions of ultralytics to perform model training and prediction (through terminal).

Things to do - 
1. Try to perform prediction on a video.
2. Create a validation dataset, to verify the results (current training shows further improvement can be achieved with more training iterations.)

<h4>Installations</h4>
Things to take care - 
1. Make sure python version is 3.8+
2. Perform pip install onnx and onnxruntime for model export.

<h4>Dataset</h4>
The dataset tested upon here composes of 30 images of golden and labrador retrievers. These two labels are the object of interest and to check the prediction test01 and test02.jpg images are used after training and validation are completed. The dataset was annotated using makesense.ai and the structure of the dataset is as described commonly for yolo architectures, i.e dataset must contain two folders images and labels.

<h4>Results</h4>
Currently, I have attached results from a successful run on the dataset. It is in the detect folder. Usually all the result are in the ultralytics folder however, to clone the repo please follow the instructions as given in the original [YOLOv8 ultralytics](https://github.com/ultralytics/ultralytics/tree/main) github repo.