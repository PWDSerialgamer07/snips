import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

"""
Just shows the histogram of an image, that's it.
Mostly for debug purpose
"""


def main(img_path) -> None:
    img = Image.open(img_path)
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original")

    # Plot grayscale histogram
    plt.subplot(1, 2, 2)
    gray_img = img.convert("L")
    plt.hist(np.array(gray_img).flatten(), bins=50, color="black")
    plt.title("Grayscale Histogram")
    plt.show()
