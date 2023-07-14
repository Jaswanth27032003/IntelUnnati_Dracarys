import subprocess

train = 'yolo task=detect mode=train epochs=100 data=data_customs.yaml model=yolov8m.pt imgsz=640 batch=4'

subprocess.run(train, shell=True)