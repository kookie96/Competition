import socket
import time

#as stated in server.py, similar things need change here
HOST = "127.0.0.1"
PORT = 1337
color = "red"
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
		
		
	
		data = s.recv(1024).decode()
        #separates 3 byte netcode from data received
		
		print(data + "\n")
		parse = data.split('$')
		
		match parse[0]:
			#Latitude
			case 'LAT':
			#	lat_raw = parse[1]
				print('lat')
				sortData(parse[1], latitude)
				
			#Longitutde 	
			case 'LON':
			#	lon_raw = parse[1]
				print('lon')
				sortData(parse[1], longitude)
				
			
			case "RGB":
				#currently it will prompt the console for a string
				color = input("color: ")
				print('color')
				
                #prints current color (for debug purposes)
				print(parse[1])
                #sends color with null terminator
				s.sendall((color + ' ').encode())	
				
			#Target state	
			case 'TGT':
			    #its sending a singular bit, so this should work right?
				#1/25/24: no it doesn't work lol
				target = True

			case 'FLA':
				sortData(parse[1], final_latitude)
			
			case 'FLO':
				sortData(parse[1], final_longitude)
#		s.sendall(('next' + ' ').encode())
		#printing lat and long to terminal for debugging purposes
		#print("lat: " + latitude + "\n" + "long: " + longitude + "\n")
		#print("########################\n")
