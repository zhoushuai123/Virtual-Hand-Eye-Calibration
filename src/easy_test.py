# Author: Mingchuan ZHOU
# Contact: mingchuan.zhou@in.tum.de
# Date: 31 Jan. 2021
# Usage: for testing the easy image from CoppeliaSim via python remoteApi
import sys
sys.path.append('python')
import numpy as np
import cv2
print('Program started')
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
        if res == vrep.simx_return_ok:
            imcount = imcount + 1
            res, rgb_resolution, rgb_image = vrep.simxGetVisionSensorImage(clientID, v0, 0, vrep.simx_opmode_buffer)
            res, depth_resolution, depth_image = vrep.simxGetVisionSensorImage(clientID, v1, 0, vrep.simx_opmode_oneshot_wait)
            rgb_img = np.array(rgb_image, dtype=np.uint8)
            depth_img = np.array(depth_image, dtype=np.uint8)
            index = []
            for i in range(depth_resolution[0] * depth_resolution[1] * 3):
                if (i % 3 != 0):
                    index.append(i)
            depth_img = np.delete(depth_img, index)
            rgb_img.resize([rgb_resolution[1], rgb_resolution[0], 3])
            depth_img.resize([depth_resolution[1], depth_resolution[0], 1])
            rgb_img = cv2.flip(rgb_img, 0)
            # depth_img = cv2.flip(depth_image, 0)
            cv2.imshow("RGB_Image", rgb_img)
            cv2.imshow("DEPTH_Image", depth_img)
            cv2.waitKey(1)
            # time.sleep(1)
            print(imcount)
        else:
            print('Failed to show rgb and depth image')
else:
    print('Failed connecting to remote API server')
print('Program ended')