import time
import drive_line

from enum import Enum
from time import sleep
from pysphero.core import Sphero
from bezier import *
from coons import *


class Type(Enum):
    DERIVATIVE = 1
    DISCRETIZATION = 2


def main():
    mac_address = "C2:03:29:02:E7:17"
    control_robot(mac_address)


def control_robot(mac_address):

    p_start = (0, 0)
    p_end = (0, 50)

    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()
        drive_line.drive_cubic_bezier(sphero, p_start, p_end, Type.DERIVATIVE)
        sphero.power.enter_soft_sleep()


if __name__ == "__main__":
    main()
