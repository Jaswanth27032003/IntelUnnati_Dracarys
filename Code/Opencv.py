import random
import cv2
from ultralytics import YOLO

# Opening the file in read mode
my_file = open("../Data/coco.txt")
# Reading the file
data = my_file.read()
# Replacing and splitting the text when newline ('\n') is seen
class_list = data.split("\n")
my_file.close()

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# Load a pretrained YOLOv8m model
model = YOLO("../Models/yolov8m.pt")

# Video file path
video_path = "../vid7.mp4"

# Output Path
output_filename = "output/vid7.avi"

capture = cv2.VideoCapture(video_path)

if not capture.isOpened():
    print("Cannot open video file")
    exit()

# Get the video properties
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video in AVI format
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Predict on the frame
    detect_params = model.predict(source=[frame], conf=0.45, save=True)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()

    # ...
    if len(DP) != 0:
        for i in range(len(DP)):
            box = DP[i].boxes[0]

            conf = box.conf[0]
            clsID = box.cls[0]
            bb = box.xyxy[0]

            pt1 = (int(bb[0]), int(bb[1]))
            pt2 = (int(bb[2]), int(bb[3]))

            cv2.rectangle(
                frame,
                pt1,
                pt2,
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

    # Write the frame to the output video
    video_writer.write(frame)

    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture and output writer
capture.release()
video_writer.release()

# Destroy all windows
cv2.destroyAllWindows()
