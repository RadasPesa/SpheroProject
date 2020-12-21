import numpy as np

from calculations import *


def linear_bezier_derivative(p0, p1, d_step):
    angles = []
    speeds = []

    for t in np.arange(0, 1 + d_step, d_step):
        angle = calculate_angle_by_derivative((p0[0], p1[0]), (p0[1], p1[1]), t)
        x_der = calculate_speed_by_derivative((p0[0], p1[0]), t)
        y_der = calculate_speed_by_derivative((p0[1], p1[1]), t)
        speed = np.sqrt((np.power(x_der, 2)) + (np.power(y_der, 2)))

        angles.append(angle)
        speeds.append(speed)

    return angles, speeds


def linear_bezier_discretization(p0, p1, d_step):
    angles = []
    speeds = []

    p0x = p0[0]
    p0y = p0[1]
    p1x = -p0[0] + p1[0]
    p1y = -p0[1] + p1[1]

    x = p0x
    y = p0y
    previous_point = (x, y)

    for t in np.arange(d_step, 1 + d_step, d_step):
        ax = t * p1x
        x = p0x + ax

        ay = t * p1y
        y = p0y + ay

        actual_point = (x, y)

        angle = calculate_angle_by_discretization(previous_point, actual_point)
        speed = calculate_speed_by_discretization(previous_point, actual_point) / d_step

        angles.append(angle)
        speeds.append(speed)

        previous_point = actual_point

    # Duplication of the last point for reaching zero speed at the end
    angle = calculate_angle_by_discretization(previous_point, previous_point)
    speed = calculate_speed_by_discretization(previous_point, previous_point) / d_step
    angles.append(angle)
    speeds.append(speed)

    return angles, speeds


def quadratic_bezier_derivative(p0, p1, p2, d_step):
    speeds = []
    angles = []

    for t in np.arange(0, 1 + d_step, d_step):
        angle = calculate_angle_by_derivative((p0[0], p1[0], p2[0]), (p0[1], p1[1], p2[1]), t)
        x_der = calculate_speed_by_derivative((p0[0], p1[0], p2[0]), t)
        y_der = calculate_speed_by_derivative((p0[1], p1[1], p2[1]), t)
        speed = np.sqrt((np.power(x_der, 2)) + (np.power(y_der, 2)))

        angles.append(angle)
        speeds.append(speed)

    return angles, speeds


def quadratic_bezier_discretization(p0, p1, p2, d_step):
    angles = []
    speeds = []

    p0x = p0[0]
    p0y = p0[1]
    p1x = -2 * p0[0] + 2 * p1[0]
    p1y = -2 * p0[1] + 2 * p1[1]
    p2x = p0[0] - 2 * p1[0] + p2[0]
    p2y = p0[1] - 2 * p1[1] + p2[1]

    x = p0x
    y = p0y
    previous_point = (x, y)

    for t in np.arange(d_step, 1 + d_step, d_step):
        t2 = t * t

        ax = t * p1x
        bx = t2 * p2x
        x = p0x + ax + bx

        ay = t * p1y
        by = t2 * p2y
        y = p0y + ay + by

        actual_point = (x, y)

        angle = calculate_angle_by_discretization(previous_point, actual_point)
        speed = calculate_speed_by_discretization(previous_point, actual_point) / d_step

        angles.append(angle)
        speeds.append(speed)

        previous_point = actual_point

    # Duplication of the last point for reaching zero speed at the end
    # CAUTION: Could be giving bad results when not drawing line
    # (connecting/connection points in standard curves must be treated)
    # possible solutions = delete every 11th value, calculate average value of previous and oncoming point
    angle = calculate_angle_by_discretization(previous_point, previous_point)
    speed = calculate_speed_by_discretization(previous_point, previous_point) / d_step
    angles.append(angle)
    speeds.append(speed)

    return angles, speeds


def cubic_bezier_derivative(p0, p1, p2, p3, d_step):
    angles = []
    speeds = []

    for t in np.arange(0, 1 + d_step, d_step):
        angle = calculate_angle_by_derivative((p0[0], p1[0], p2[0], p3[0]), (p0[1], p1[1], p2[1], p3[1]), t)
        x_der = calculate_speed_by_derivative((p0[0], p1[0], p2[0], p3[0]), t)
        y_der = calculate_speed_by_derivative((p0[1], p1[1], p2[1], p3[1]), t)
        speed = np.sqrt((np.power(x_der, 2)) + (np.power(y_der, 2)))

        angles.append(angle)
        speeds.append(speed)

    return angles, speeds


def cubic_bezier_discretization(p0, p1, p2, p3, d_step):
    speeds = []
    angles = []

    p0x = p0[0]
    p0y = p0[1]
    p1x = -3 * p0[0] + 3 * p1[0]
    p1y = -3 * p0[1] + 3 * p1[1]
    p2x = 3 * p0[0] - 6 * p1[0] + 3 * p2[0]
    p2y = 3 * p0[1] - 6 * p1[1] + 3 * p2[1]
    p3x = -p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]
    p3y = -p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]

    x = p0x
    y = p0y
    previous_point = (x, y)

    for t in np.arange(d_step, 1 + d_step, d_step):
        t2 = t * t
        t3 = t2 * t

        ax = t * p1x
        bx = t2 * p2x
        cx = t3 * p3x
        x = p0x + ax + bx + cx

        ay = t * p1y
        by = t2 * p2y
        cy = t3 * p3y
        y = p0y + ay + by + cy

        actual_point = (x, y)

        angle = calculate_angle_by_discretization(previous_point, actual_point)
        speed = calculate_speed_by_discretization(previous_point, actual_point) / d_step

        angles.append(angle)
        speeds.append(speed)

        previous_point = actual_point

    # Duplication of the last point for reaching zero speed at the end
    angle = calculate_angle_by_discretization(previous_point, previous_point)
    speed = calculate_speed_by_discretization(previous_point, previous_point) / d_step
    angles.append(angle)
    speeds.append(speed)

    return angles, speeds
