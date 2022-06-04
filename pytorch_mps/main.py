from time import time

import torch


def main():
    device = torch.device("mps")

    print(device)

    x1 = torch.randn(500, 500).to(device)
    x2 = torch.randn(500, 500).to(device)

    start = time()
    for _ in range(5000):
        x1 @ x2
    print(f"On GPU: {time() - start:.2f}")

    y1 = torch.randn(500, 500)
    y2 = torch.randn(500, 500)

    start = time()
    for _ in range(5000):
        y1 @ y2
    print(f"On CPU: {time() - start:.2f}")

if __name__ == "__main__":
    main()
