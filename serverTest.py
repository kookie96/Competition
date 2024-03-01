from server import comms
import threading
from time import sleep
HOST = "127.0.0.1"


def GPS():
    global latitude
    global longitude
    global altitude
    latitude = "33.837189"
    longitude = "-84.53877"
    altitude = "416"
    print("GPS Done!")
    return (latitude, longitude, altitude)


def AI():
    global pixelX
    global pixelY
    pixelX = "2000"
    pixelY = "1125"
    sleep(10)
    print("AI Done!")
    return (pixelX, pixelY)


def SENSOR():
    global azimuth
    global rollAngle
    global theta
    azimuth = "172"
    rollAngle = "0"
    theta = "-36"
    print("SENSORS DONE!")
    return (azimuth, rollAngle, theta)


try:
    t1 = threading.Thread(None, GPS())
    t2 = threading.Thread(None, AI())
    t3 = threading.Thread(None, SENSOR())
    t1.start()
    t2.start()
    t3.start()
    t2.join()
    t1.join()
    t2.join()
except:
    pass

comms(HOST, latitude, longitude, altitude,
      azimuth, pixelX, pixelY, rollAngle, theta)
