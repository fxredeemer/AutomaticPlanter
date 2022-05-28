import machine
import utime

maxHysteresis = 4
humidityThreshold = 50000
led = machine.Pin(25, machine.Pin.OUT)


class Pot:
    def __init__(self, input, output):
        self.input = machine.ADC(input)
        self.output = machine.Pin(output, machine.Pin.OUT)
        self.title = f"In: {input} | Out: {output}"
        self.enabled = False
        self.hysteresis = 0
    
    def Set(self, enabled):
        oldState = self.enabled

        if oldState and (not enabled):
            self.hysteresis = self.hysteresis - 1
        
        if (enabled):
            self.hysteresis = maxHysteresis

        self.enabled = self.hysteresis > 0

    def GetState(self):
        return f"Enabled: {self.enabled} | Hyst: {self.hysteresis}"

pots = [
    Pot(26, 19),
    # Pot(27, 20),
]

def ReadHumidity(humiditySensor):
    return humiditySensor.read_u16()

def CheckPumpEnablingNecessary(humidity):
    return humidity < humidityThreshold

def SetPumpState(pump, enable):
    pump.value(enable)

while True:
    utime.sleep(1)
    led.toggle()
    for pot in pots:
        humidity = ReadHumidity(pot.input)

        pot.Set(CheckPumpEnablingNecessary(humidity))   
        SetPumpState(pot.output, pot.enabled)

        print(pot.title)
        print(humidity)
        print(pot.GetState())
        print()
    print("-------------------------------------") 