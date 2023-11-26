import os
from os.path import join

temporary_path = join(os.path.dirname(os.path.realpath(__file__)), "temporary")
img_path = join(os.path.dirname(os.path.realpath(__file__)), "imgs")

for file in os.listdir(img_path):
    if file.endswith(".png"):
        with open("badges.svg", "r") as f:

            content = f.read()
            content = content.replace("IMAGE_LINK", join(img_path, file))

            destination = join(temporary_path, file.replace(".png", ".svg"))

            with open(destination, "w") as f:
                f.write(content)
