from PIL import Image
import os

input = 'sprites'        
output = 'sprites_scaled'   
scale_by = 10               

if not os.path.exists(output):
    os.makedirs(output)

for i in os.listdir(input):
    input_path = os.path.join(input, i)
    img = Image.open(os.path.join(input, i))
    new_size = (img.width * scale_by, img.height * scale_by)
    resized_img = img.resize(new_size, Image.NEAREST)
    output_path = os.path.join(output, i)
    resized_img.save(output_path)
