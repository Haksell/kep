from math import sqrt


def iterative():
    G = 9.81
    DT = 3e-5

    x = 1.0
    t = v = 0.0
    while x > 0.0:
        dy = 2.0 * x
        slope = sqrt(1 + dy**2)
        a = G * dy / slope
        v += a * DT
        x -= v * DT / slope
        t += DT
    return t


def main():
    print(f"{iterative():.6f}")


if __name__ == "__main__":
    main()
