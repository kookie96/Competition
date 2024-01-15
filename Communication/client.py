#note, must install dearpygui
import socket
import time
import dearpygui.dearpygui as dpg

#as stated in server.py, similar things need change here
HOST = "127.0.0.1"
PORT = 6969
color = "red"
target = False
latitude = ''
longitude = ''
rt_time = 0
#inb4 out of scope


#sets up GUI
dpg.create_context()

def change_color(sender, callback):
	return

with dpg.window(label="Primary Telemetry"):
      	dpg.add_text("color of target")
      	dpg.add_input_text(default_value="red")
      	dpg.add_button(label="send",callback=FUNCTION)
      	dpg.add_text("target found?")
      	dpg.add_text(target)
      	dpg.add_text("latitude: " + latitude)
      	dpg.add_text("longitude: " + longitude)
		dpg.add_text("ping " + rt_time + "ms")
        
        
dpg.create_viewport(title="Primary Telemetry", width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()



try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        
		
        #connects to server
		s.connect((HOST, PORT))
		target = s.recv(1)
		s.sendall(b"recieved")
		#takes note of time for rt_time
		ping_time = time.time()
        latitude = ''
		longitude = ''
		
        
		####experimental netcode section####
		
		#receives first piece of data and notes time for rtt
		data = s.recv(1024)
		pong_time = time.time()

		parse = data.split("$")
		
		match parse[0]:
			#Latitude
			case "LAT":
				lat_raw = parse[1]
				for space in lat_raw:
			if space == ' ':
				break
			else:
				latitude += space
				
			#Longitutde 	
			case "LON":
				lon_raw = parse[1]
				for space in data:
			if space == ' ':
				break
			else:
				latitude += space
				
			#case "RGB":
				
				
			#Target state	
			case "TGT":
				
		#calculates round trip time
		#probaby can't be considered an accurate "ping" but it's just a general measurement
		rt_time  = (pong_time - ping_time)*1000
		
		#until the GUI works, I'm just going to spit the lat and long into the terminal
		print("lat: " + latitude + "\n" + "long: " + longitutde "\n")
		print("########################\n")
		dpg.start_dearpigui()
except: KeyboardInterrupt
	dpg.destroy_context()
    exit()
print(rtt_time)




