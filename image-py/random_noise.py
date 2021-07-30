import random
from pathlib import Path

from classopt import ClassOpt, config
from PIL import Image
import numpy as np

from metrics import mse


@ClassOpt
class Opt:
    input_img_path: Path
    random_range: int = config(long=True, default=10)


def main(opt: Opt):
    img = np.array(Image.open(opt.input_img_path))
    height, width, dim = img.shape
    print(f"{height=}, {width=}, {dim=}")

    new_img = random_noise(img, opt.random_range)

    result = mse(img, new_img)
    print(f"mse={result}")

    Image.fromarray(new_img).show()


def random_noise(img: np.ndarray, random_range: int) -> np.ndarray:
    new_img = np.zeros_like(img)
    height, width, dim = img.shape

    for y in range(height):
        for x in range(width):
            new_img[y, x] += img[y, x] + np.array(
                [random.randint(-random_range, random_range) for _ in range(dim)],
                dtype="uint8",
            )
            new_img[y, x] = np.clip(new_img[y, x], 0, 255)

    return new_img


if __name__ == "__main__":
    opt = Opt.from_args()
    main(opt)
