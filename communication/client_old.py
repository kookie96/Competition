import socket
import time

#as stated in server.py, similar things need change here
HOST = "127.0.0.1"
PORT = 6969
color = "red"
target = False
latitude = ''
longitude = ''
final_latitude = ''
final_longitude = ''
rt_time = 0
#inb4 out of scope

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        
		
        #connects to server
		s.connect(HOST, PORT)
		target = s.recv(1)
		s.sendall(b"recieved")
		#takes note of time for rt_time
		ping_time = time.time()
        latitude = ''
		longitude = ''
		
		
		#receives first piece of data and notes time for rtt
		data = s.recv(1024)
		pong_time = time.time()
        
        #separates 3 byte netcode from data received
		parse = data.split("$")
		
		match parse[0]:
			#Latitude
			case 'LAT':
			#	lat_raw = parse[1]
				for space in parse[1]:
		        	if space == ' ':
			        	break
		        	else:
			        	latitude += space
				
			#Longitutde 	
			case 'LON':
			#	lon_raw = parse[1]
				for space in parse[1]:
	        		if space == ' ':
			        	break
		        	else:
			        	latitude += space
				
			case "RGB":
                #prints current color (for debug purposes)
			    print(parse[1])
                #sends color with null terminator
                s.sendall(b(color + ' '))	
				
			#Target state	
			case 'TGT':
			    #its sending a singular bit, so this should work right?
                target = parse[1]
            case 'FLA':
                for space in parse[1]:
                    if space == ' ':
                        break
                    else:
                        final_latitude += space
            case 'FLO':
                for space in parse[1]:
                    if space == ' ':
                        break
                    else:
                        final_longitude += space
             	
		#calculates round trip time
		#probaby can't be considered an accurate "ping" but it's just a general measurement
		rt_time  = (pong_time - ping_time)*1000
		print("ping: " + rt_time)
		#printing lat and long to terminal for debugging purposes
		print("lat: " + latitude + "\n" + "long: " + longitutde "\n")
		print("########################\n")
except KeyboardInterrupt:
    exit()





