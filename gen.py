import os

folder = "sprites"  # Folder containing your sprite images
images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
images.sort()  # Optional: sort the images alphabetically

columns = 5  # Number of images per row

with open("GALLERY.md", "w") as f:
    f.write("# Sprite Gallery\n\n")
    f.write("<table>\n")
    for i, image in enumerate(images):
        if i % columns == 0:
            f.write("  <tr>\n")
        f.write(f'    <td><img src="{folder}/{image}" alt="{image}" width="150"></td>\n')
        if (i + 1) % columns == 0:
            f.write("  </tr>\n")
    if len(images) % columns != 0:
        f.write("  </tr>\n")
    f.write("</table>\n")
