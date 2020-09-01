import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json
from tqdm import tqdm



path_to_frames = '../frames/'
fps = 15  # determined by ffmpeg






with open('../landmarks.json') as json_file:
    landmarks = json.load(json_file)

    for frame, faces in tqdm(landmarks.items()):
        file_name = "../frames/out{:05d}.png".format(int(frame)+1)
        for face, points in faces.items():
            if face == "0":

                fig, ax = plt.subplots(1, 2)
                fig.suptitle("Frame number: {}".format(frame))
                # first plot the regular image
                img = mpimg.imread(file_name)
                ax[0].imshow(img)
                ax[0].set_title("Original")
                ax[0].axis('off')
                ax[0].grid('off')

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
                ax[1].plot(x[0:16+1], y[0:16+1], color='b')
                # right eyebrow
                ax[1].plot(x[17:21+1], y[17:21+1], color='b')
                # left eyebrow
                ax[1].plot(x[22:26+1], y[22:26+1], color='b')
                # nose
                ax[1].plot(np.concatenate((x[27:30+1], [x[33]])), np.concatenate((y[27:30+1], [y[33]])), color='b')
                # nostrils
                ax[1].plot(x[31:35+1], y[31:35+1], color='b')
                # right eye
                ax[1].plot(np.concatenate((x[36:41+1], [x[36]])), np.concatenate((y[36:41+1], [y[36]])), color='b')
                # left eye
                ax[1].plot(np.concatenate((x[42:47+1], [x[42]])), np.concatenate((y[42:47+1], [y[42]])), color='b')
                # upper lip, upper line
                ax[1].plot(x[48:54+1], y[48:54+1], color='b')
                # lower lip, lower line
                ax[1].plot(x[55:59+1], y[55:59+1], color='b')
                # upper lip, lower line
                ax[1].plot(x[60:64+1], y[60:64+1], color='b')
                # lower lip, upper line
                ax[1].plot(x[65:], y[65:], color='b')



                ax[1].set_title('Landmarks')
                ax[1].set_xlim(-1, 1)
                ax[1].set_ylim(-1, 1)
                ax[1].set_aspect('equal')
                ax[1].grid('off')
                ax[1].axis('off')

                plt.savefig("./frames/out-{:04d}.png".format(int(frame)+1))
