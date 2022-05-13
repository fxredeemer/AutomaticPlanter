import machine
import utime

humidityThreshold = 20000
led = machine.Pin(20, machine.Pin.OUT)
humiditySensor = machine.ADC(26)

def ReadHumidity():
    return humiditySensor.read_u16()

def ToggleLed():
    led.toggle()

def CheckPumpEnablingNecessary(humidity):
    return humidity < humidityThreshold

def SetPumpState(enable):
    led.value(enable)

while True:
    utime.sleep(1)
    humidity = ReadHumidity()
    enablePumpNecessary = CheckPumpEnablingNecessary(humidity)
    SetPumpState(enablePumpNecessary)

