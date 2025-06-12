from handler import RoboflowHandler

handler = RoboflowHandler("defect-detection-b2xj1")

# handler.upload_dataset("./dataset")

# settings = {
#     "preprocessing": {
#         "resize": {"width": 640, "height": 640, "format": "Stretch to"}
#     },
#     "augmentation": {
#         "image": { "versions": 1 }, 
#         "blur": { "pixels": 1.5 },
#         "rgrayscale": { "percent": 50 },
#         "saturation": { "percent": 50 }
#     }
# }
# version = handler.generate_version(settings)


# To see what versions are available. There should only be one, and the one that we will use.
# print(handler.get_our_project().list_versions())
version = handler.get_our_project().version(2)
model = handler.train_model(version=version)

