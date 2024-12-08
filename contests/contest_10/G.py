from math import hypot, log, sqrt

G = 9.81


def acceleration():
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


def conservation():
    E = G
    STEPS = 1234
    L = (2 * sqrt(5) + log(2 + sqrt(5))) / 4
    DL = L / STEPS

    y = 1.0
    t = 0.0
    for _ in range(STEPS):
        dy = 2 * sqrt(y)
        ny = y - dy / hypot(1, dy) * DL
        v0 = sqrt(2 * (E - G * y))
        v2 = sqrt(2 * (E - G * ny))
        v1 = (v0 + v2) / 2
        y = max(0, ny)
        t += DL / v1

    return t


def nomath(y):
    STEPS = 1 << 15
    e = y * G
    dy = y / STEPS
    t = 0.0
    for _ in range(STEPS):
        my = y - (dy / 2)
        dydx = 2 * sqrt(my)
        v = sqrt(2 * (e - G * my))
        vy = v * (dydx / hypot(1, dydx))
        dt = dy / vy
        y -= dy
        t += dt

    return t


def main():
    print(f"{acceleration():.6f}")
    print(f"{conservation():.6f}")
    print(f"{nomath(1.0):.6f}")


if __name__ == "__main__":
    main()
