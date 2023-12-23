from ultralytics import YOLO

model = YOLO('traffic light detection\\models\\TLDv2\\TLDv2.pt')

results = model(source=0, show=True, conf=0.4, save=True)  # generator of results