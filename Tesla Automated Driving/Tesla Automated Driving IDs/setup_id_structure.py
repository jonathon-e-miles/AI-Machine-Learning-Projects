import os
import numpy as np
from PIL import Image

# 1. Define categories based on your project
categories = ['Pedestrian', 'Vehicle', 'Stop_Sign', 'Traffic_Light', 'Cyclist']
base_folder = 'sample_images'

print("🏗️ Building sample directory structure...")

for category in categories:
    path = os.path.join(base_folder, category)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    
    # Generate 5 dummy images per category
    for i in range(1, 6):
        file_name = f'sample_{category.lower()}_{i}.jpg'
        full_path = os.path.join(path, file_name)
        
        # Create a 224x224 random color image
        random_color = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        img = Image.fromarray(random_color)
        img.save(full_path)

print(f"✅ DONE! Created '{base_folder}' with {len(categories)} subfolders.")
