<H2> YOLO Object Detection Using Custom Dataset </H2>

This is a simple project where by using YOLOv8 a custom dataset is classified based on the object of interest. The following have been completed - 
1. Successfully ran the basic yolo predict and train based on the instructions provided in the ultralytics README.md.
2. Used different yaml files to test against different datasets, such as VisDrone, COCO and OpenImagesV7.
3. Built a custom dataset using [makesense.ai](https://www.makesense.ai/) and downloaded the images from google.
4. Wrote a python script based on instructions of ultralytics to perform model training and prediction (through terminal).

Things to do - 
1. Try to perform prediction on a video.
2. Create a validation dataset, to verify the results (current training shows further improvement can be achieved with more training iterations.)

# Installations
Things to take care - 
1. Make sure python version is 3.8+
2. Perform pip install onnx and onnxruntime for model export.

# Results
Currently, I have attached results from a successful run on the dataset. It is in the ultralytics folder.

# Dataset creation
The dataset is created in the following format - 

<p>Dataset</p>
    |
    ---- dogs
          |
          ---- images
          |       |
          |       ----train
          |            <img1>
          |            <img2>
          |               
          ---- labels
                 |
                 ----train
                       <img1.txt>
                       <img2.txt>