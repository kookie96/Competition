import socket
import time

HOST = "127.0.0.003"
PORT = 1337

color = "red"
altitude = "416"
latitude = "33.837189"
longitude = "-84.53877"
azimuth = "172"
pixelX = "2000"
pixelY = "1125"
rollAngle = "0"
theta = "-36"
target = True
sent_target = False


# function for taking data and cutting off everything past the null terminator
def sortData(raw, variable):
    for space in raw:
        if space == " ":
            break
        else:
            variable += space


def comms(HOST, latitude, longitude, altitude, azimuth, pixelX, pixelY, rollAngle, theta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # sets up listener for client
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        global color
        global sent_target
    # this is when the client is connected to the server
        with conn:
            print(f"Connected by {addr}")

        # requests color
            color_state = "RGB$" + color
            conn.sendall(color_state.encode())

            color_data = conn.recv(1024).decode()
            print("recieve 1")
            color = ""

            # decodes color
            sortData(color_data, color)

            while True:
                try:
                    # sends if the target is aquired or not
                    # target_state = 'TGT$' + target
                    # conn.sendall(target_state)

                    # adds null terminator and netcode for client to parse
                    # ackage = ""
                    # ackage = "LAT$" + str(latitude) + "\n"
                    # latitude += 1
                    # rint(package)
                    # onn.sendall(package.encode())

                    # makes sure client recieves first coordnate before sending the second coordnate

                    # package = ""
                    # package = "LON$" + str(longitude) + "\n"
                    # conn.sendall(package.encode())

                    # if the target is found and lat/long is calculated, the coordnates of the target will be sent
                    if target and not (sent_target):
                        # conn.sendall(package.encode())
                        # time.sleep(0.003)

                        package = "LAT$" + str(latitude) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "LON$" + str(longitude) + " "
                        conn.sendall(package.encode())
                       # print(package)
                        time.sleep(0.003)
                        package = "ALT$" + str(altitude) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "AZI$" + str(azimuth) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "PIX$" + str(pixelX) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "PIY$" + str(pixelY) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "ROL$" + str(rollAngle) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "THA$" + str(theta) + " "
                        conn.sendall(package.encode())
                        time.sleep(0.003)
                       # print(package)
                        package = "TGT$" + "if you read this"
                        conn.sendall(package.encode())
                        sent_target = True
                       # print(package)
                        exit()
                except KeyboardInterrupt:
                    exit()
                # except (BrokenPipeError, IOError):
                break       # print(BrokenPipeError)
