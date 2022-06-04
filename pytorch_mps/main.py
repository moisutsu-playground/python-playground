from time import time

import torch


def main():
    device = torch.device("mps")

    print(device)

    size = 8192

    x1 = torch.randn(size, size).to(device)
    x2 = torch.randn(size, size).to(device)

    start = time()
    for _ in range(10):
        x1 @ x2
    print(f"On GPU: {time() - start:.2f}")

    y1 = torch.randn(size, size)
    y2 = torch.randn(size, size)

    start = time()
    for _ in range(10):
        y1 @ y2
    print(f"On CPU: {time() - start:.2f}")

if __name__ == "__main__":
    main()
