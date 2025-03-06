from PIL import Image
import os

input_folder = 'sprites'          # Folder with your original 16x16 sprites
output_folder = 'sprites_scaled'    # Folder to save the resized sprites
scale_factor = 10                   # 16x16 becomes 160x160

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        input_path = os.path.join(input_folder, filename)
        img = Image.open(input_path)
        new_size = (img.width * scale_factor, img.height * scale_factor)
        resized_img = img.resize(new_size, Image.NEAREST)
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)
        print(f"Resized {filename} to {new_size}")
