from openAthena import *

setCamera(24, 4000, 2250, 0,0,0,0,0,1,"cobb.tif")
lat,long,alt,terAlt = calcCoord(33.837189, -84.53877, 418, 172,-36, 2000, 1125, 0)
print(lat)
print(long)
print(alt)
print(terAlt)