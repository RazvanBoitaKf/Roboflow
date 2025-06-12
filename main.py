from roboflow_handler import RoboflowHandler

handler = RoboflowHandler("defect-detection-b2xj1")

handler.upload_dataset("C:/Users/eu/dataset")

settings = {
    "preprocessing": {
        "resize": {"width": 640, "height": 640, "format": "Stretch to"}
    },
    "augmentation": {
        "image": { "versions": 1 }, 
        "blur": { "pixels": 1.5 },
        "rgrayscale": { "percent": 50 },
        "saturation": { "percent": 50 }
    }
}
version = handler.generate_version(settings)