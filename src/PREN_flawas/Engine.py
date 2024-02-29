import json, time

__config = {
    "Solenoid": [
        {
            "Red": 16,
            "Yellow": 20,
            "Blue": 26,
            "Weight": 23
        }, {
            "DelayColors": 0.2,
            "DelayWeight": 0.2
        }
    ],
    "Stepperengine": [
        {
        "Enable": 5,
        "Direction": 6,
        "Step": 13,
        "DelaySteps": 0.004,
        "NumberOfSteps": 800
        }
    ],
    "Piezo": [{
        "GIPO": 12,
        "Time": 2
    }],
    "Inputs": [
        {
            "Start" : 27,
            "EmergencyStop": 22
        }
    ]
}

__pos = {
    "Yellow": 1,
    "Red": 2,
    "Blue": 3
}

__AllActors = [__config["Solenoid"][0]["Red"], __config["Solenoid"][0]["Blue"], __config["Solenoid"][0]["Yellow"],
               __config["Solenoid"][0]["Weight"], __config["Stepperengine"][0]["Enable"]]

def __init__(self):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(__config["Solenoid"][0]["Yellow"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Red"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Blue"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Weight"], GPIO.OUT)

    GPIO.setup(__config["Stepperengine"][0]["Enable"], GPIO.OUT)
    GPIO.setup(__config["Stepperengine"][0]["Direction"], GPIO.OUT)
    GPIO.setup(__config["Stepperengine"][0]["Step"], GPIO.OUT)

    GPIO.setup(__config["Piezo"][0]["GIPO"], GPIO.OUT)
    GPIO.setup(__config["Inputs"][0]["Start"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(__config["Inputs"][0]["EmergencyStop"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(__config["Inputs"][0]["EmergencyStop"], GPIO.FALLING, callback=button_pressed_callback, bouncetime=100)
    PiezoPin = GPIO.PWM(__config["Piezo"][0]["GIPO"], 100)


def button_pressed_callback(channel):
    print("Emergency pressed")
    GPIO.output(__AllActors, GPIO.LOW)
    #->Rückmeldung für Display

def turnRight():
    GPIO.out(Enable, GPIO.LOW)
    for i in range(NumberOfSteps):
        GPIO.output(Direction, GPIO.LOW)
        GPIO.output(Step, GPIO.HIGH)
        time.sleep(DelaySteps)
        GPIO.output(Step, GPIO.LOW)
    GPIO.out(Enable, GPIO.HIGH)
    incrementPosition()

def turnLeft():
    GPIO.out(Enable, GPIO.LOW)
    for x in range(NumberOfSteps):
        GPIO.output(Direction, GPIO.HIGH)
        GPIO.output(Step, GPIO.HIGH)
        time.sleep(DelaySteps)
        GPIO.output(Step, GPIO.LOW)
    GPIO.out(Enable, GPIO.HIGH)
    #Todo: Decrement function

def incrementPosition():
    if __pos["Yellow"] == 4:
        __pos["Yellow"] = 1
    else:
        __pos["Yellow"] = __pos["Yellow"] + 1
    if __pos["Red"] == 4:
        __pos["Red"] = 1
    else:
        __pos["Red"] = __pos["Red"] + 1
    if __pos["Blue"] == 4:
        __pos["Blue"] = 1
    else:
        __pos["Blue"] = __pos["Blue"] + 1

def solYellow():
    GPIO.output(__config["Solenoid"][0]["Yellow"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Yellow"], GPIO.LOW)

def solRed():
    GPIO.output(__config["Solenoid"][0]["Red"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Red"], GPIO.LOW)

def solBlue():
    GPIO.output(__config["Solenoid"][0]["Blue"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Blue"], GPIO.LOW)

def solWeight():
    GPIO.output(__config["Solenoid"][0]["Weight"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayWeight"])
    GPIO.output(__config["Solenoid"][0]["Weight"], GPIO.LOW)