import machine
import utime

humidityThreshold = 20000
led = machine.Pin(13, machine.Pin.OUT)

out19 = machine.Pin(19, machine.Pin.OUT)
out20 = machine.Pin(20, machine.Pin.OUT)

in26 = machine.ADC(26)
in27 = machine.ADC(27)

pots = [
    ( in26, out19 ),
    ( in27, out20 ),
]

def ReadHumidity(humiditySensor):
    return humiditySensor.read_u16()

def CheckPumpEnablingNecessary(humidity):
    return humidity < humidityThreshold

def SetPumpState(pump, enable):
    pump.value(enable)

while True:
    utime.sleep(1)
    led.Togge()
    for pot in pots:
        inPin = pot[0]
        outPin = pot[1]
        humidity = ReadHumidity(inPin)
        enablePumpNecessary = CheckPumpEnablingNecessary(humidity)
        SetPumpState(outPin, enablePumpNecessary)
        print(humidity)
        print(enablePumpNecessary)
        print()
    print("-------------------------------------") 


#7:15