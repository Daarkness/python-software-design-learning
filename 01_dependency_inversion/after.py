from abc import ABC,abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        '''抽象子类必须要实现的方法'''
    @abstractmethod
    def turn_off(self):
        '''抽象子类必须要实现的方法'''

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")



class ElectricPowerSwitch:

    def __init__(self,l:Switchable) -> None:
        # 依赖的类 从 固定的 LightBulb 改为 Switchable
        # 我们可以系新建一个Switchable 的抽线子类，达到功能修改的目的
        self.client  = l
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self. on = False

        else:
            self.client.turn_on()
            self.on = True
l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()