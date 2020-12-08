import numpy as np

from calculations import *


def coons_derivative(p0, p1, p2, p3, d_step):
    speeds = []
    angles = []

    k = 1 / 6

    for t in np.arange(0, 1 + d_step, d_step):
        angle = calculate_angle_by_derivative_coons((p0[0], p1[0], p2[0], p3[0]), (p0[1], p1[1], p2[1], p3[1]), t)
        x_der = calculate_speed_by_derivative_coons((p0[0], p1[0], p2[0], p3[0]), t)
        y_der = calculate_speed_by_derivative_coons((p0[1], p1[1], p2[1], p3[1]), t)
        speed = k * (np.sqrt((np.power(x_der, 2)) + (np.power(y_der, 2))))

        angles.append(angle)
        speeds.append(speed)

    return angles, speeds


def coons_discretization(p0, p1, p2, p3, d_step):
    speeds = []
    angles = []

    k = 1 / 6

    p0x = p0[0] + 4 * p1[0] + p2[0]
    p0y = p0[1] + 4 * p1[1] + p2[1]
    p1x = -3 * p0[0] + 3 * p2[0]
    p1y = -3 * p0[1] + 3 * p2[1]
    p2x = 3 * p0[0] - 6 * p1[0] + 3 * p2[0]
    p2y = 3 * p0[1] - 6 * p1[1] + 3 * p2[1]
    p3x = -p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]
    p3y = -p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]

    x = k * p0x
    y = k * p0y
    previous_point = (x, y)

    for t in np.arange(d_step, 1 + d_step, d_step):
        t2 = t * t
        t3 = t2 * t

        ax = t * p1x
        bx = t2 * p2x
        cx = t3 * p3x
        x = k * (p0x + ax + bx + cx)

        ay = t * p1y
        by = t2 * p2y
        cy = t3 * p3y
        y = k * (p0y + ay + by + cy)

        actual_point = (x, y)

        angle = calculate_angle_by_discretization(previous_point, actual_point)
        speed = calculate_speed_by_discretization(previous_point, actual_point) / d_step

        angles.append(angle)
        speeds.append(speed)

        previous_point = actual_point

    return angles, speeds
