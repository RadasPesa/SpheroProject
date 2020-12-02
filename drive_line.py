import time

from time import sleep
from pysphero.core import Sphero
from bezier import *
from coons import *
from drive import Type


def drive_linear_bezier(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    angles = []
    speeds = []

    if type.value == 1:
        angles, speeds = linear_bezier_derivative(p0, p1, d_step)
    elif type.value == 2:
        angles, speeds = linear_bezier_discretization(p0, p1, d_step)

    start_time = time.time()
    for i in range(0, len(angles)):
        print("Angle: " + str(angles[i]))
        print("Speed: " + str(speeds[i]))
        time.sleep(0.3 - ((time.time() - start_time) % 0.3))


def drive_quadratic_bezier(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    midpoint = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)

    angles = []
    speeds = []
    angles2 = []
    speeds2 = []

    if type.value == 1:
        angles, speeds = quadratic_bezier_derivative(p0, p0, midpoint, d_step)
        angles2, speeds2 = quadratic_bezier_derivative(midpoint, p1, p1, d_step)
    elif type.value == 2:
        angles, speeds = quadratic_bezier_discretization(p0, p0, midpoint, d_step)
        angles2, speeds2 = quadratic_bezier_discretization(midpoint, p1, p1, d_step)

    angles += angles2
    speeds += speeds2

    start_time = time.time()
    for i in range(0, len(angles)):
        print("Angle: " + str(angles[i]))
        print("Speed: " + str(speeds[i]))
        time.sleep(0.15 - ((time.time() - start_time) % 0.15))


def drive_cubic_bezier(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    angles = []
    speeds = []

    if type.value == 1:
        angles, speeds = cubic_bezier_derivative(p0, p0, p1, p1, d_step)
    elif type.value == 2:
        angles, speeds = cubic_bezier_discretization(p0, p0, p1, p1, d_step)

    start_time = time.time()
    for i in range(0, len(angles)):
        print("Angle: " + str(angles[i]))
        print("Speed: " + str(speeds[i]))
        time.sleep(0.3 - ((time.time() - start_time) % 0.3))


def drive_coons(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    angles = []
    speeds = []
    angles2 = []
    speeds2 = []
    angles3 = []
    speeds3 = []

    if type.value == 1:
        angles, speeds = coons_derivative(p0, p0, p0, p1, d_step)
        angles2, speeds2 = coons_derivative(p0, p0, p1, p1, d_step)
        angles3, speeds3 = coons_derivative(p0, p1, p1, p1, d_step)
    elif type.value == 2:
        angles, speeds = coons_discretization(p0, p0, p0, p1, d_step)
        angles2, speeds2 = coons_discretization(p0, p0, p1, p1, d_step)
        angles3, speeds3 = coons_discretization(p0, p1, p1, p1, d_step)

    angles += angles2
    angles += angles3
    speeds += speeds2
    speeds += speeds3

    start_time = time.time()
    for i in range(0, len(angles)):
        print("Angle: " + str(angles[i]))
        print("Speed: " + str(speeds[i]))
        time.sleep(0.1 - ((time.time() - start_time) % 0.1))
