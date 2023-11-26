import os
import random
from os.path import join

temporary_path = join(os.path.dirname(os.path.realpath(__file__)), "temporary")
img_path = join(os.path.dirname(os.path.realpath(__file__)), "imgs")
output_path = join(os.path.dirname(os.path.realpath(__file__)), "outputs")


def random_color_hex():

    return "%06x" % random.randint(0, 0xFFFFFF)


for file in os.listdir(img_path):
    if file.endswith(".png"):
        with open("badges.svg", "r") as f:

            content = f.read()
            content = content.replace("IMAGE_LINK", join(img_path, file))
            content = content.replace("BORDER_COLOR", random_color_hex())
            content = content.replace("FILL_COLOR", random_color_hex())

            destination = join(temporary_path, file.replace(".png", ".svg"))

            if os.path.exists(destination):
                continue

            with open(destination, "w") as f:
                f.write(content)

for file in os.listdir(temporary_path):
    if file.endswith(".svg"):
        os.system(
            f"inkscape {join(temporary_path, file)} -D -o {join(output_path, file.replace('.svg', '.png'))} "
        )
