import time

from time import sleep
from pysphero.core import Sphero
from bezier import *
from coons import *


def main():
    mac_address = "C2:03:29:02:E7:17"
    control_robot(mac_address)


def control_robot(mac_address):
    with Sphero(mac_address=mac_address) as sphero:
        wake_robot(sphero)
        drive_curve(sphero)
        sleep(2)
        sleep_robot(sphero)


def wake_robot(sphero: Sphero):
    sphero.power.wake()


def sleep_robot(sphero: Sphero):
    sphero.power.enter_soft_sleep()


def drive_curve(sphero: Sphero):
    d_step = 0.1

    p0 = (0, 0)
    p1 = (0, 0)
    p2 = (10, 0)
    p3 = (10, 0)

    angles, speeds = cubic_bezier_derivative(p0, p1, p2, p3, d_step)

    start_time = time.time()
    for i in range(0, len(angles)):
        time.sleep(0.1 - ((time.time() - start_time) % 0.1))
        print("Angle: " + str(angles[i]))
        print("Speed: " + str(speeds[i]))


if __name__ == "__main__":
    main()
