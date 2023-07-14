# IntelUnnati_Dracarys
Enhancing road safety with YOLOv8m object detection improves road safety with real-time object detection in challenging conditions.
# Road Object Detection using YOLOv8m
The Road Object Detection using YOLOv8m repository is a computer vision project that aims to detect and classify objects on the road using the YOLOv8m (You Only Look Once) object detection algorithm. This project leverages the power of deep learning and real-time object detection to enhance road safety, assist autonomous vehicles, and improve traffic management. With a specific focus on addressing challenging weather conditions such as fog and rain, the project aims to enhance the model's ability to accurately detect objects in adverse road environments. By incorporating advanced techniques and data augmentation methods, the repository strives to improve the robustness and reliability of object detection in low-visibility situations. By leveraging the YOLOv8m model architecture, the repository provides a comprehensive solution for training, evaluating, and deploying the model, empowering users to apply it in various road safety applications, traffic management systems, and autonomous driving solutions.

## Installation

1) Create a Python virtual environment using the following command:
 
   `python -m venv /path/to/new/virtual/environment`

2) Activate the virtual environment by running the appropriate command based on your operating system:

   **For Windows:**
       `\path\to\new\virtual\environment\Scripts\activate`

     **For macOS and Linux:**
      `source /path/to/new/virtual/environment/bin/activate`

3) Install the ultralytics library using pip:

      `pip install ultralytics`

4) Download the YOLOv8m model from the Ultralytics repository. You can find the model at
[https://github.com/ultralytics/ultralytics]
Download the appropriate model weights file and place it in the project directory.

6) Download images for training and testing purposes using the simple_image_download library. Install the library using pip:

    `pip install simple_image_download`

      Once installed, run the code snippet provided in the project documentation to download images related to vehicles in snowy and rainy conditions. The images will be          saved in a specific directory.

6) Annotate the downloaded images using the labelImg tool. Install the tool using pip:

      `pip install labelImg`
   
      Run the labelImg command in the command prompt, which will open a window to annotate the images. Open each image and draw bounding boxes around the vehicles, labeling       them with the corresponding class. Save the annotated images in a separate folder.

8) Create a data.yaml file to specify the dataset configuration. Add the classes to the data.yaml file as mentioned in the provided classes.txt file.

9) Create two folders, train and val. Inside each folder, create images and labels subfolders. Copy the annotated images and corresponding label files into their respective folders.

10) Train the model using the YOLO command:

      `yolo task=detect mode=train epochs=100 data=data_customs.yaml model=yolov8m.pt imgsz=640 batch=4`

**Note: If you have an Nvidia graphics card with GPU support and the latest CUDA and PyTorch versions, the training process will be faster. However, if you are using a CPU, the training process may take a longer time to complete.**

11) After training, you can predict the output on images and videos. Use the following command to predict and save the output:

      `yolo task=detect mode=predict model=yolov8m.pt show=True conf=0.5 source=image_source`

      This command will save the output in the current directory, inside a `"runs" `folder.

**Now we added OpenCv to our Project**

  1) Create a Directory "OpenCv" which contains all the open files of `Models`, `Code`, `Data`at one place to integrate Yolo with OpenCv
  2) Now open the command prompt and activate the Python Environment you have created. Ex: `Enivornment_name\Scripts\activate`
  3) Now change Directory to the OpenCv folder Ex: `cd Directory_location/Opencv`
  4) Now refer to the OpenCv code `Code/Opencv.py`

**Note: To get the desired output you have to change the code to your requirements in `Line 6, Line 22, Line 25, Line 39`
    `Line 6` - Data/coco.txt
    `Line 22` - Weights/yolov8m.pt
    `Line 25` - Video Path.mp4
    `Line 39` - Output Path.avi**
    

  **Note: For `Line 39` you have to create a folder and then save the output to that folder Ex: `output/vid1.mp4` and the video will save in the .avi format. Every time u run the code you have to give the same output location but you have to change the name of the file, If you doesn't change the name it will overide the previous output file with the current output file every time you run you will see only one result in the output folder.**

  
  
### Please Carefully refer to the ReadMe file for detailed usage instructions and customization options.
