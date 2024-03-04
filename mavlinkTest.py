from pymavlink import mavutil
print('attempting to connect')
mavDevice = mavutil.mavlink_connection('/dev/ttyUSB0', baud = 57600)
print('connected')
while True:
    mavDevice.mav.param_request_list_send()
    
    mavTest = mavDevice.recv() 
    #altitude = mavutil.decode(b)

    print(f'Altitude = {mavTest}')
