import math


def calculate_angle_by_derivative(points_x, points_y, t):
    angle = 0

    if len(points_x) == 2:
        # Linear
        u = points_x[1] - points_x[0]
        v = points_y[1] - points_y[0]

        angle = math.atan2(v, u) * 180 / math.pi
    elif len(points_x) == 3:
        # Quadratic
        u = 2 * (points_x[1] - points_x[0]) + 2 * (points_x[0] - 2 * points_x[1] + points_x[2]) * t
        v = 2 * (points_y[1] - points_y[0]) + 2 * (points_y[0] - 2 * points_y[1] + points_y[2]) * t

        angle = math.atan2(v, u) * 180 / math.pi
    elif len(points_x) == 4:
        # Cubic
        t2 = t * t

        part1x = (1 - t) * (1 - t) * (points_x[1] - points_x[0])
        part2x = 2 * t * (1 - t) * (points_x[2] - points_x[1])
        part3x = t2 * (points_x[3] - points_x[2])
        u = part1x + part2x + part3x

        part1y = (1 - t) * (1 - t) * (points_y[1] - points_y[0])
        part2y = 2 * t * (1 - t) * (points_y[2] - points_y[1])
        part3y = t2 * (points_y[3] - points_y[2])
        v = part1y + part2y + part3y

        angle = math.atan2(v, u) * 180 / math.pi
    else:
        print("Error in calculating speed by derivative")

    if angle < 0:
        angle = math.fabs(angle)
    else:
        angle = 360 - angle

    return angle


def calculate_speed_by_derivative(points, t):
    der = 0

    if len(points) == 2:
        # Linear
        w0 = -1
        w1 = 1

        der = (points[0] * w0) + (points[1] * w1)
    elif len(points) == 3:
        # Quadratic
        w0 = -2 * (1 - t)
        w1 = 2 - (4 * t)
        w2 = 2 * t

        der = (points[0] * w0) + (points[1] * w1) + (points[2] * w2)
    elif len(points) == 4:
        # Cubic
        w0 = -3 * math.pow((1 - t), 2)
        w1 = 9 * math.pow(t, 2) - 12 * t + 3
        w2 = 3 * (2 - 3 * t) * t
        w3 = 3 * math.pow(t, 2)

        der = (points[0] * w0) + (points[1] * w1) + (points[2] * w2) + (points[3] * w3)
    else:
        print("Error in calculating speed by derivative")

    return der


def calculate_angle_by_discretization(prev_point, act_point):
    angle = math.atan2((act_point[1] - prev_point[1]), (act_point[0] - prev_point[0])) * 180 / math.pi

    if angle < 0:
        angle = math.fabs(angle)
    else:
        angle = 360 - angle

    return angle


def calculate_speed_by_discretization(prev_point, act_point):
    Dx = math.pow((act_point[0] - prev_point[0]), 2)
    Dy = math.pow((act_point[1] - prev_point[1]), 2)

    speed = math.sqrt(Dx + Dy)

    return speed
