from ultralytics import YOLO

model = YOLO('traffic light detection\\models\\TLDv2.pt')

print("model architecture:", model.model)

params = list(model.model.parameters())
print("parameters", params)

print("class names", model.names)

# results = model(source=0, show=True, conf=0.2, save=True, stream=True)  # generator of results

