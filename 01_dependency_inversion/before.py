class LightBulb:
    def turn_on(self):
        print("LightBule: turned on..")
    
    def turn_off(self):
        print("LightBule: turned off ..")


class ElectriPowerSwitch:

    def __init__(self,l:LightBulb) -> None:
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self. on = False

        else:
            self.lightBulb.turn_on()
            self.on = True

        
lb = LightBulb()
switch = ElectriPowerSwitch(lb)
switch.press()
switch.press()