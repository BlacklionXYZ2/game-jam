from math import sin, cos
#Not sure what the classes will look like so I'll just make generalised functions for now
def rotate(pos, angle):
    sine = sin(angle)
    cosine = cos(angle)
    pos = (pos[0]*cosine + pos[1]*sine, pos[1]*cosine - pos[0]*sine)