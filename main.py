from handler import RoboflowHandler

handler = RoboflowHandler("defect-detection-b2xj1")

# Upload the dataset only if the pictures don't exist. Duplicates won't get added to the roboflow dataset anyways. 
# handler.upload_dataset("./dataset")

# If a version already exists, check instructions below to see what version id exists. Use the method below to get the version,
# instead of creatign a new version every time.

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

