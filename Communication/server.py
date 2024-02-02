import socket
import time

HOST = "127.0.0.1"
PORT = 1337

color = 'red'
latitude = 0
longitude = 0
final_latitude = 0
final_longitude = 0
target = False
sent_target = False
#function for taking data and cutting off everything past the null terminator
def sortData(raw, variable):
	for space in raw:
		if space == ' ':
			break
		else:
			variable += space


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #sets up listener for client
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
   
    #this is when the client is connected to the server
	with conn:
		
		print(f"Connected by {addr}")
		
		#requests color
		color_state = 'RGB$' + color
		conn.sendall(color_state.encode())
		
		color_data = conn.recv(1024).decode()
		print('recieve 1')
		color = ''
				
		#decodes color
		sortData(color_data, color) 
		
		while True:
			try:
                
				
                #sends if the target is aquired or not
                #target_state = 'TGT$' + target
                #conn.sendall(target_state)


                #adds null terminator and netcode for client to parse
				package = ''
				package = ('LAT$' + str(latitude) + '\n')
				latitude += 1
				print(package)
				conn.sendall(package.encode())
				time.sleep(0.005)
                #makes sure client recieves first coordnate before sending the second coordnate
				
				
				package = ''
				package = 'LON$' + str(longitude) + '\n'
				conn.sendall(package.encode())
				
				#if the target is found and lat/long is calculated, the coordnates of the target will be sent
				if (target && !sent_target):
					package = ('TGT$' + 'if you read this')
					conn.sendall(package.encode())
					time.sleep(0.003)
					
					package = ('FLA$' + str(final_latitude) + ' ')
					conn.sendall(package.encode())
					time.sleep(0.003)
					
					package = ('FLO$' + str(final_longitude) + ' ')
					conn.sendall(package.encode())
					sent_target = True
					
			except KeyboardInterrupt:
				exit()
