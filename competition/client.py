import socket
import time
from openAthena import *
import decimal
# as stated in server.py, similar things need change here
HOST = "127.0.0.1"
PORT = 1337

color = "red"
target = False
latitude = ''
longitude = ''
altitude = ''
azimuth = ''
pixelX = ''
pixelY = ''
rollAngle = ''
theta = ''
thetaoffset = 35  # change later, estimated camera inclination
# inb4 out of scope

# function for taking data and cutting off everything past the null terminator


def sortData(raw, variable):
    for space in raw:
        if space == ' ':
            break
        else:
            variable += space


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connects to server
    s.connect((HOST, PORT))

    while target:
        latitude = ''
        longitude = ''
        altitude = ''
        azimuth = ''
        pixelX = ''
        pixelY = ''
        rollAngle = ''
        theta = ''

        data = s.recv(4096).decode()
    # separates 3 byte netcode from data received

        print(data + "\n")
        parse = data.split('$')

        match parse[0]:
            # Latitude
            case 'LAT':
                print('lat')
                sortData(parse[1], latitude)

            # Longitutde
            case 'LON':
                print('lon')
                sortData(parse[1], longitude)
            case 'ALT':
                print('alt')
                sortData(parse[1], longitude)
            case 'AZI':
                print('azi')
                sortData(parse[1], azimuth)
            case 'PIX':
                print('pix')
                sortData(parse[1], pixelX)
            case 'PIY':
                print('piy')
                sortData(parse[1], pixelY)
            case 'ROL':
                print('rol')
                sortData(parse[1], rollAngle)
            case 'THA':
                print('tha')
                sortData(parse[1], theta)

            case "RGB":
                # currently it will prompt the console for a string
                color = input("color: ")
                print('color')

        # prints current color (for debug purposes)
                print(parse[1])
        # sends color with null terminator
                s.sendall((color + ' ').encode())

            # Target state
            case 'TGT':
                # its sending a singular bit, so this should work right?
                # 1/25/24: no it doesn't work lol
                target = True

            # s.sendall(('next' + ' ').encode())
        # printing lat and long to terminal for debugging purposes
        # print("lat: " + latitude + "\n" + "long: " + longitude + "\n")
        # print("########################\n"u)
        print(longitude)
        print(latitude)
        print(altitude)
        print(theta)
        print(azimuth)
        print(rollAngle)
        print(pixelX)
        print(pixelY)
        setCamera(24, 4000, 1125, 0, 0, 0, 0, 0, 1, "cobb.tif")
        lat, long, alt, terAlt = calcCoord(
            latitude, longitude, altitude, azimuth, theta, pixelX, pixelY, rollAngle)
        print(lat)
        print(long)
        print(alt)
        print(terAlt)
        # #
        #
