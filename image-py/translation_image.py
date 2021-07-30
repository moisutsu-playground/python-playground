from pathlib import Path

from classopt import ClassOpt, config
from PIL import Image
import numpy as np

from metrics import mse


@ClassOpt
class Opt:
    input_img_path: Path
    move_x: int = config(long=True, default=10)
    move_y: int = config(long=True, default=10)


def main(opt: Opt):
    img = np.array(Image.open(opt.input_img_path))
    height, width, dim = img.shape
    print(f"{height=}, {width=}, {dim=}")

    new_img = translation_img(img, opt.move_x, opt.move_y)

    result = mse(img, new_img)
    print(f"mse={result}")

    Image.fromarray(new_img).show()


def translation_img(img: np.ndarray, move_x: int, move_y: int) -> np.ndarray:
    new_img = np.copy(img)
    height, width, _ = img.shape

    for y in range(height):
        for x in range(width):
            new_img[y, x] = img[
                (y + move_y + height) % height, (x + move_x + width) % width
            ]

    return new_img


if __name__ == "__main__":
    opt = Opt.from_args()
    main(opt)
