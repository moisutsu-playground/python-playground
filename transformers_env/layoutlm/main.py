from pathlib import Path

from PIL import Image
from transformers import AutoModel, AutoProcessor

processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base")
model = AutoModel.from_pretrained("microsoft/layoutlmv3-base")

image_path = Path("dataset/samples/bert.jpg")

image = Image.open(image_path).convert("RGB")

encoding = processor(image, return_tensors="pt", truncation=True, max_length=512)

outputs = model(**encoding)
last_hidden_states = outputs.last_hidden_state

print(last_hidden_states)
