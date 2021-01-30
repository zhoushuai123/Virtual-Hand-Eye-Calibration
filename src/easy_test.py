import sys
# import open3d as o3d
sys.path.append('python')
import time
import array
import numpy as np
import cv2
print('Program started')
import sim
try:
    import sim as vrep
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')
import time
print('Program started')
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:
    print('Connected to remote API server')
    res, v0 = vrep.simxGetObjectHandle(clientID, 'Vision_global_rgb', vrep.simx_opmode_oneshot_wait)
    res, v1 = vrep.simxGetObjectHandle(clientID, 'Vision_global_depth', vrep.simx_opmode_oneshot_wait)
    res, resolution, image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_streaming)
    imcount = 0
    while (vrep.simxGetConnectionId(clientID) != -1):
        res, resolution, image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_buffer)
        # res, resolution_rgb, image_rgb = vrep.simxGetVisionSensorImage(clientID, v2, 0, vrep.simx_opmode_buffer)
        if res == vrep.simx_return_ok:
            # res = vrep.simxSetVisionSensorImage(clientID, v1, image, 0, vrep.simx_opmode_oneshot)
            imcount = imcount + 1
            res, resolution, image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_buffer)
            img = np.array(image, dtype=np.uint8)
            img.resize([resolution[1], resolution[0], 3])
            img = cv2.flip(img, 0)
            cv2.imshow("Test",img)
            cv2.waitKey(1)
            print(imcount)
else:
    print('Failed connecting to remote API server')
print('Program ended')


