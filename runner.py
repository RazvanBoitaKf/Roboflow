from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="PLACEHOLDER"
)

result = client.run_workflow(
    workspace_name="kf-hlml3",
    workflow_id="custom-workflow",
    images={
        "image2": "dataset/test/atest5.png"
    },
    use_cache=True
)

print(result)
with open('dataset/classes.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

first_prediction = result[0]['predictions']['predictions'][0]
class_id = first_prediction['class_id']
confidence = first_prediction['confidence']

class_name = classes[class_id]

print(f"Class ID: {class_id}")
print(f"Class Name: {class_name}")
print(f"Confidence: {confidence:.4f}")