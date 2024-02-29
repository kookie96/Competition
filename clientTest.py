from client import comms, camera
HOST = "127.0.0.1"
DEMFILENAME = "cobb.tif"
camera(24, 4000, 2250, 0, 0, 0, 0, 0, 1, DEMFILENAME)
lat, long, alt, terAlt = comms(HOST)
print(lat)
print(long)
print(alt)
print(terAlt)
