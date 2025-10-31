import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Load ImageNet classes
try:
    with open('imagenet_classes.txt', 'r') as f:
        CLASSES = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    CLASSES = [f'class_{i}' for i in range(1000)]

# Load pretrained GoogLeNet model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = models.googlenet(weights=models.GoogLeNet_Weights.IMAGENET1K_V1)
model = model.to(device)
model.eval()

# Image preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def classify_image(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        img_tensor = preprocess(img).unsqueeze(0).to(device)
        
        with torch.no_grad():
            outputs = model(img_tensor)
        
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        top_k = torch.topk(probabilities, 5)
        
        results = []
        for i in range(5):
            class_idx = top_k.indices[0][i].item()
            confidence = top_k.values[0][i].item() * 100
            results.append({
                'class': CLASSES[class_idx] if class_idx < len(CLASSES) else f'class_{class_idx}',
                'confidence': f'{confidence:.2f}%'
            })
        
        return results, None
    except Exception as e:
        return None, str(e)