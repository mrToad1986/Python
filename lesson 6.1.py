from time import sleep


class TrafficLight:
    __color = 'black'

    def running(self):
        while True:
            print('\r', f'\x1b[5;41;30m{"stop"}\x1b[0m', sep='', end='')  # красный
            sleep(7)
            print('\r', f'\x1b[5;43;30m{"wait"}\x1b[0m', sep='', end='')  # желтый
            sleep(2)
            print('\r', f'\x1b[5;42;30m{" go "}\x1b[0m', sep='', end='')  # зеленый
            sleep(5)


trafficLight = TrafficLight()
trafficLight.running()
