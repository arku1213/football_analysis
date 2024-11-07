from ultralytics import YOLO
model = YOLO('yolov8s')

results = model.predict('input_videos/test (10).mp4', save = True)
print(results[0])
print('===========================')
for box in results[0].boxes:
    print(box)
print("hello world")