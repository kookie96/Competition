import socket
import time
from openAthena import *
import decimal
# as stated in server.py, similar things need change here
HOST = '127.0.0.1'
PORT = 1337
global color
color = 'red'
thetaoffset = 0  # change later, estimated camera inclination
# inb4 out of scope

# function for taking data and cutting off everything past the null terminator


def sortData(raw, variable):
    for space in raw:
        if space == " ":
            break
        else:
            variable += space


def camera(focal, X, Y, k1, k2, k3, p1, p2, aspectRatio, DEMFILENAME):
    setCamera(focal, X, Y, k1, k2, k3, p1, p2, aspectRatio, DEMFILENAME)


def communication(HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # connects to server
        s.connect((HOST, PORT))
        target = True
        while target:
            global latitude
            global longitude
            global altitude
            global azimuth
            global pixelX
            global pixelY
            global rollAngle
            global theta

            data = s.recv(1024).decode()
    # separates 3 byte netcode from data received

            # print(data + '\n')
            parse = data.split('$')

            match parse[0]:
                # Latitude
                case 'LAT':
                   # print('lat')
                    # so    rtData(parse[1], latitude)
                    latitude = parse[1]
                   # print(latitude)
            # Longitutde
                case 'LON':
                   # print('lon')
                    # sortData(parse[1], longitude)
                    longitude = parse[1]
                   # print(longitude)
                case 'ALT':
                   # print('alt')
                    # sortData(parse[1], altitude)
                    altitude = parse[1]
                   # print(altitude)
                case 'AZI':
                   # print('azi')
                    # sortData(parse[1], azimuth)
                    azimuth = parse[1]
                   # print(azimuth)
                case 'PIX':
                   # print('pix')
                    # sortData(parse[1], pixelX)
                    pixelX = parse[1]
                   # print(pixelX)
                case 'PIY':
                   # print('piy')
                    # sortData(parse[1], pixelY)
                    pixelY = parse[1]
                   # print(pixelY)
                case 'ROL':
                   # print('rol')
                    # sortData(parse[1], rollAngle)
                    rollAngle = parse[1]
                   # print(rollAngle)
                case 'THA':
                   # print('tha')
                    # sortData(parse[1], theta)
                    theta = parse[1]
                   # print(theta)
                case 'RGB':
                    # currently it will prompt the console for a string
                    color = input('color: ')
                   # print('color')

        # prints current color (for debug purposes)
                    # print(parse[1])
        # sends color with null terminator
                    s.sendall((color + ' ').encode())

            # Target state
                case 'TGT':
                    # its sending a singular bit, so this should work right?
                    # 1/25/24: no it doesn't work lol
                    target = False

            # s.sendall(('next' + ' ').encode())
        # printing lat and long to terminal for debugging purposes
        # print('lat: ' + latitude + "\n" + "long: " + longitude + "\n")
        # print('########################\n'u)
   # print(longitude)
   # print(latitude)
   # print(altitude)
   # print(theta)
   # print(azimuth)
    # print(rollAngle)
   # rint(pixelX)
   # print(pixelY)
    lat, long, alt, terAlt = calcCoord(
        latitude, longitude, altitude, azimuth, (decimal.Decimal(theta)-decimal.Decimal(thetaoffset)), pixelX, pixelY, rollAngle)
   # print(lat)
   # print(long)
   # print(alt)
   # print(terAlt)
    return (lat, long, alt, terAlt)


def comms(HOST):
    while (True):
        try:
            lat, long, alt, terAlt = communication(HOST)
            time.sleep(0.1)
        except (UnboundLocalError):
            #   print("Could not fin:wqd server.")
            print(Exception)
            break
        except ConnectionRefusedError:
            pass
        else:
            finLat, finLong, finAlt, finterAlt = lat, long, alt, terAlt
            # print("This code actually executed!")
            # break
            return (finLat, finLong, finAlt, finterAlt)
    return (lat, long, alt, terAlt)
