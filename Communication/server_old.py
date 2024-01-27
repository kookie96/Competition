import socket
import time
import serial


#CURRENT LIST OF VARIABLES THAT NEED TO CHANGE
#-Host IP
#-port

#Host ip will be configured (hopefully) at a later date, any port can be used as long as its >1023
#Host ip is what we set the static ip of the pi on primary to be.

#Ground station will be the client, the ground pi will be the router and will give the primary
#pi its ip. The groundstation computer will not need a static ip, only the ip to the pi on primary.
#
#the current ip and port are by no means the final. As of writing this the host ip is currently the
#loopback address
#
#
HOST = "127.0.0.1"
PORT = 6969

color = 'red'
gps = serial.Serial('/dev/serial0', 9600, timeout=1)
target = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #sets up listener for client
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    #this is when the client is connected to the server
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                #requests color
                color_state = 'RGB$' + color
                color_data = conn.recv(1024)
                for space in color_data
                    if space == ' ':
                        break
                    else:
                        latitude += space

                #sends if the target is aquired or not
                target_state = 'TGT$' + target
                conn.sendall(target_state)
                confirm = conn.recv(4)
                if (confirm == 'next'):
                    break
                
                #reads off of GPS module
                gps_line = gps.readline().decode('utf-8').strip()

                print(gps_line)
                
                #parses the GPS module with the NMEA code $GNGGA
                if gps_line.startswith('$GNGGA'):
                    
                    #it divides the datapoints into an array of strings
                    fields = gps_line.split(',')
                    
                    latitude= fields[3]
                    longitude = fields[5]
                    
                    #adds null terminator and netcode for client to parse
                    package = 'LAT$' + latitude + ' '
                    
                    conn.sendall(b(package))
                    
                    #makes sure client recieves first coordnate before sending the second coordnate
                    next_package = conn.recv(4)
                    if next_package == 'next':
                        package = 'LON$' longitude + ' '
                        conn.sendall(b(package))
                    
                    
                
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(b"pong")
            except KeyboardInterrupt:
                gps.close()
                exit()
