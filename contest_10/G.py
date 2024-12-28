from math import hypot, sqrt

G = 9.81


def acceleration(*, x, dt):
    t = v = 0.0
    while x > 0.0:
        dy = 2.0 * x
        slope = sqrt(1 + dy**2)
        a = G * dy / slope
        v += a * dt
        x -= v * dt / slope
        t += dt
    return t


def conservation_dy(*, x, steps):
    y = x**2
    e = y * G
    dy = y / steps
    t = 0.0
    for _ in range(steps):
        my = y - dy / 2
        dydx = 2 * sqrt(my)
        s = sqrt(2 * (e - G * my))
        sy = s * (dydx / hypot(1, dydx))
        dt = dy / sy
        y -= dy
        t += dt
    return t


def conservation_dx(*, x, steps):
    e = x**2 * G
    dx = x / steps
    t = 0.0
    for _ in range(steps):
        mx = x - dx / 2
        s = sqrt(2 * (e - G * mx**2))
        sx = s / hypot(1, 2 * mx)
        dt = dx / sx
        x -= dx
        t += dt
    return t


def conservation_ds(*, x, steps):
    e = x**2 * G
    fs = sqrt(2 * e)
    ds = fs / steps
    s = t = 0.0
    for _ in range(steps):
        y0 = (e - 1 / 2 * s**2) / G
        y1 = max(0, (e - 1 / 2 * (s + ds) ** 2) / G)
        x0 = sqrt(y0)
        x1 = sqrt(y1)
        ms = s + ds / 2
        dt = hypot(x0 - x1, y0 - y1) / ms
        s += ds
        t += dt
    return t


def main():
    print(f"{acceleration(x=1.0, dt=1e-5):.6f}")
    print(f"{conservation_dy(x=1.0, steps=10**4):.6f}")
    print(f"{conservation_dx(x=1.0, steps=10**4):.6f}")
    print(f"{conservation_ds(x=1.0, steps=10**2):.6f}")


if __name__ == "__main__":
    main()
