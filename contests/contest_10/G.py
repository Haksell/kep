from math import hypot, log, sqrt

G = 9.81


def acceleration():
    DT = 3e-6

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


def nomathy(*, x, steps):
    y = x**2
    e = y * G
    dy = y / steps
    t = 0.0
    for _ in range(steps):
        my = y - dy / 2
        dydx = 2 * sqrt(my)
        v = sqrt(2 * (e - G * my))
        vy = v * (dydx / hypot(1, dydx))
        dt = dy / vy
        y -= dy
        t += dt
    return t


def nomathx(*, x, steps):
    e = x**2 * G
    dx = x / steps
    t = 0.0
    for _ in range(steps):
        mx = x - dx / 2
        v = sqrt(2 * (e - G * mx**2))
        vx = v / hypot(1, 2 * mx)
        dt = dx / vx
        x -= dx
        t += dt
    return t


def nomathv(*, x, steps):
    e = x**2 * G
    dv = sqrt(2 * e) / steps
    v = t = 0.0
    for _ in range(steps):
        y0 = (e - 1 / 2 * v**2) / G
        y1 = max(0, (e - 1 / 2 * (v + dv) ** 2) / G)
        x0 = sqrt(y0)
        x1 = sqrt(y1)
        mv = v + dv / 2
        dt = hypot(x0 - x1, y0 - y1) / mv
        v += dv
        t += dt
    return t


def main():
    print(f"{acceleration():.6f}")
    print(f"{conservation():.6f}")
    print(f"{nomathy(x=1.0, steps=100):.6f}")
    print(f"{nomathx(x=1.0, steps=100):.6f}")
    print(f"{nomathv(x=1.0, steps=100):.6f}")


if __name__ == "__main__":
    main()
