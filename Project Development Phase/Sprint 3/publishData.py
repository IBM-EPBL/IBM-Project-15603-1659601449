# Python code

# IMPORT SECTION STARTS

import wiotp.sdk.device # python -m pip install wiotp
import time
import random

# IMPORT SECTION ENDS
# -----------------------------------------------
# API CONFIG SECTION STARTS

myConfig = {
    "identity" : {
        "orgId" : "b7lu7v",
        "typeId" : "Weather_Monitoring",
        "deviceId" : "Id12345"
    },
    "auth" : {
        "token" : "12345678"
    }
}

# API CONFIG SECTION ENDS
# -----------------------------------------------
# FUNCTIONS SECTION STARTS

def myCommandCallback(cmd):
    print("recieved cmd : ",cmd)


def logData2Cloud(location,temperature,visibility):
    client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
    client.connect()
    repo=random.randint(0,5)
    if repo==1:
        prt="SLOW DOWN , SCHOOL IS NEAR"
    elif repo==3:
        prt="SLOW DOWN , HOSPITAL NEARBY"
    elif repo==5:
        prt="NEED HELP, POLICE STATION NEARBY"
    else:
        prt=""
    speed=random.randint(0,150)
    if speed>=100:
        prt3="SLOW DOWN , Speed Limit Exceeded"
    elif speed>=60 and speed<100:
        prt3="Moderate Speed"
    else:
        prt3="Usual speed limit"
    sign=random.randint(0,5)
    if sign==1:
        prt2="Right Diversion ->"
    elif sign==3:
        prt2="Left Diversion <-"
    elif sign==5:
        prt2="U Turn"
    else:
        prt2=""
    if temperature<=50:
        prt4="Fog Ahead, Drive Slow"
    else:
        prt4="Clear Weather"

    client.publishEvent(eventId="status",msgFormat="json",data={
        "temperature" : temperature,
        "speedlimit" : visibility,"Message":prt, "Sign":prt2, "Speed":prt3, "Visibility":prt4,
        "location" : location
    },qos=0,onPublish=None)  
    client.commandCallback = myCommandCallback
    client.disconnect()

# FUNCTIONS SECTION ENDS
