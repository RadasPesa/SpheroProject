from time import sleep

from pysphero.core import Sphero
from pysphero.constants import Toy
from pysphero.utils import toy_scanner


def main():
    mac_address = "C2:03:29:02:E7:17"
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()
        sleep(2)
        sphero.power.enter_soft_sleep()


if __name__ == "__main__":
    main()
