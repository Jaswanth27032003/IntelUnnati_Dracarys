from ultralytics import YOLO
import numpy

model = YOLO("../Models/yolov8m.pt")

images = ["../4.jpeg", "../5.jpeg", "../15.jpeg", "../16.jpeg", "../17.jpeg", "../23.jpeg", "../24.jpeg"]

detection_output =  model.predict(source=images, conf=0.5, save=True)

print(detection_output)

print(detection_output[0].numpy())