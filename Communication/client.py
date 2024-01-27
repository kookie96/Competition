import socket
import time

#as stated in server.py, similar things need change here
HOST = "127.0.0.1"
PORT = 6969
color = 'blue'
target = False
latitude = ''
longitude = ''
final_latitude = ''
final_longitude = ''
#inb4 out of scope

#function for taking data and cutting off everything past the null terminator
def sortData(raw, variable):
	for space in raw:
		if space == ' ':
			break
		else:
			variable += space


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        
	#connects to server
	s.connect((HOST, PORT))
	
	while True:
		latitude = ''
		longitude = ''
		
		
		print('receive 1')
		data = s.recv(1024).decode()
        #separates 3 byte netcode from data received
		
		print(data + "\n")
		parse = data.split('$')
		
		match parse[0]:
			#Latitude
			case 'LAT':
			#	lat_raw = parse[1]
				print('lat')
				for space in parse[1]:
					if space == ' ':
						break
					else:
						latitude += space
				
			#Longitutde 	
			case 'LON':
			#	lon_raw = parse[1]
				print('lon')
				for space in parse[1]:
					if space == ' ':
						break
					else:
						latitude += space
				
			case "RGB":
				print('color')
                #prints current color (for debug purposes)
				print(parse[1])
                #sends color with null terminator
				s.sendall((color + ' ').encode())	
				
			#Target state	
			case 'TGT':
			    #its sending a singular bit, so this should work right?
				#1/25/24: no it doesn't work lol
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
		data = ''
#		s.sendall(('next' + ' ').encode())
		#printing lat and long to terminal for debugging purposes
		#print("lat: " + latitude + "\n" + "long: " + longitude + "\n")
		#print("########################\n")