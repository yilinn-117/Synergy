from ultralytics import YOLO
from PIL import Image

model = YOLO('yolov8m.pt')

results = model.predict(source='0', show = True)