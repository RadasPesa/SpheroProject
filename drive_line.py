import time

from pysphero.core import Sphero
from bezier import *
from coons import *
from drive import Type
from pysphero.driving import Direction
from robot_calculations import *

time_per_section = 0.1  # in seconds


def drive_linear_bezier(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    angles = []
    speeds = []

    if type.value == 1:
        angles, speeds = linear_bezier_derivative(p0, p1, d_step)
    elif type.value == 2:
        angles, speeds = linear_bezier_discretization(p0, p1, d_step)

    angles = transform_robot_angle(angles)

    angles = [int(round(i)) for i in angles]
    speeds = [int(round(i)) for i in speeds]

    print(angles)
    print(speeds)

    section_time = time_per_section * 3
    start_time = time.time()
    print("Starting driving")
    for i in range(0, len(angles)):
        sphero.driving.drive_with_heading(speeds[i], angles[i], Direction.forward)
        time.sleep(section_time - ((time.time() - start_time) % section_time))

    # Stopping sphero (might be deleted after consultation)
    sphero.driving.drive_with_heading(0, int(angles[len(angles) - 1]), Direction.forward)
    print("Ending driving")


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

        angles[0] = angles[1]
        angles2[len(angles2)-1] = angles2[len(angles2)-2]
    elif type.value == 2:
        angles, speeds = quadratic_bezier_discretization(p0, p0, midpoint, d_step)
        angles2, speeds2 = quadratic_bezier_discretization(midpoint, p1, p1, d_step)

    angles += angles2
    speeds += speeds2

    angles = transform_robot_angle(angles)

    angles = [int(round(i)) for i in angles]
    speeds = [int(round(i)) for i in speeds]

    print(angles)
    print(speeds)

    section_time = time_per_section * 1.5
    start_time = time.time()
    print("Starting driving")
    for i in range(0, len(angles)):
        sphero.driving.drive_with_heading(speeds[i], angles[i], Direction.forward)
        time.sleep(section_time - ((time.time() - start_time) % section_time))

    print("Ending driving")


def drive_cubic_bezier(sphero: Sphero, p0, p1, type: Type):
    d_step = 0.1

    angles = []
    speeds = []

    if type.value == 1:
        angles, speeds = cubic_bezier_derivative(p0, p0, p1, p1, d_step)

        angles[0] = angles[1]
        angles[len(angles)-1] = angles[len(angles)-2]
    elif type.value == 2:
        angles, speeds = cubic_bezier_discretization(p0, p0, p1, p1, d_step)

    angles = transform_robot_angle(angles)

    angles = [int(round(i)) for i in angles]
    speeds = [int(round(i)) for i in speeds]

    print(angles)
    print(speeds)

    section_time = time_per_section * 3
    start_time = time.time()
    print("Starting driving")
    for i in range(0, len(angles)):
        sphero.driving.drive_with_heading(speeds[i], angles[i], Direction.forward)
        time.sleep(section_time - ((time.time() - start_time) % section_time))

    print("Ending driving")


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

        angles[0] = angles[1]
        angles3[len(angles3)-1] = angles3[len(angles3)-2]
    elif type.value == 2:
        angles, speeds = coons_discretization(p0, p0, p0, p1, d_step)
        angles2, speeds2 = coons_discretization(p0, p0, p1, p1, d_step)
        angles3, speeds3 = coons_discretization(p0, p1, p1, p1, d_step)

    angles += angles2
    angles += angles3
    speeds += speeds2
    speeds += speeds3

    angles = transform_robot_angle(angles)

    angles = [int(round(i)) for i in angles]
    speeds = [int(round(i)) for i in speeds]

    print(angles)
    print(speeds)

    section_time = time_per_section
    start_time = time.time()
    print("Starting driving")
    for i in range(0, len(angles)):
        sphero.driving.drive_with_heading(speeds[i], angles[i], Direction.forward)
        time.sleep(section_time - ((time.time() - start_time) % section_time))

    print("Ending driving")
