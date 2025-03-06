import os

sprites = [f for f in os.listdir("sprites_scaled")]
columns = 10 

with open("GALLERY.md", "w") as f:
    f.write("# Sprite Gallery\n\n")
    f.write("<table>\n")
    for i, s in enumerate(sprites):
        if i % columns == 0:
            f.write("  <tr>\n")
        f.write(f'    <td><img src="sprites_scaled/{s}" alt="{s}" width="160"></td>\n')
        if (i + 1) % columns == 0:
            f.write("  </tr>\n")
    if len(sprites) % columns != 0:
        f.write("  </tr>\n")
    f.write("</table>\n")
