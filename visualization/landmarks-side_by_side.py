import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm



path_to_frames = '../frames/'
fps = 15  # determined by ffmpeg






with open('../landmarks.json') as json_file:
    landmarks = json.load(json_file)
    plt.figure()
    for frame, faces in landmarks.items():
        plt.cla()
        plt.title("Frame number: {}".format(frame))
        for face, points in faces.items():
            if face == "0":
                points = np.array(points)[0]
                points = points
                x = points[:, 0]
                y = -points[:, 1]

                x_cm = np.mean(x)
                y_cm = np.mean(y)

                # center by the average
                x = x - x_cm
                y = y - y_cm

                x = np.array(x)
                y = np.array(y)

                # # point 39 is inner right eye and point 42 is inner left eye
                # d = np.sqrt((x[42]-x[39])**2+(y[42]-y[39])**2)
                # x = x/d
                # y = y/d

                # plt.scatter(x, y, color='b', marker='.')
                # for i in range(len(x)):
                #     plt.annotate(i, [x[i], y[i]])

                # NOTE array slices do NOT include final index
                # jaw
                plt.plot(x[0:16+1], y[0:16+1], color='b')
                # right eyebrow
                plt.plot(x[17:21+1], y[17:21+1], color='b')
                # left eyebrow
                plt.plot(x[22:26+1], y[22:26+1], color='b')
                # nose
                plt.plot(np.concatenate((x[27:30+1], [x[33]])), np.concatenate((y[27:30+1], [y[33]])), color='b')
                # nostrils
                plt.plot(x[31:35+1], y[31:35+1], color='b')
                # right eye
                plt.plot(np.concatenate((x[36:41+1], [x[36]])), np.concatenate((y[36:41+1], [y[36]])), color='b')
                # left eye
                plt.plot(np.concatenate((x[42:47+1], [x[42]])), np.concatenate((y[42:47+1], [y[42]])), color='b')
                # upper lip, upper line
                plt.plot(x[48:54+1], y[48:54+1], color='b')
                # lower lip, lower line
                plt.plot(x[55:59+1], y[55:59+1], color='b')
                # upper lip, lower line
                plt.plot(x[60:64+1], y[60:64+1], color='b')
                # lower lip, upper line
                plt.plot(x[65:], y[65:], color='b')




                plt.xlim(-1, 1)
                plt.ylim(-1, 1)
                plt.gca().set_aspect('equal')
                plt.pause(1e-9)
