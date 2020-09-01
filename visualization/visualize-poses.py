import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm


with open('../poses.json') as json_file:
    poses = json.load(json_file)
    for frame, humans in poses.items():
        plt.cla()
        plt.title("Frame number: {}".format(frame))
        for id, human in humans.items():
            part_nums = list(human.keys())
            bodyparts = list(human.values())
            points = []
            scores = []
            for part in bodyparts:
                dataline = part.split('-')
                data = dataline[1].split(")")
                coords = data[0].split('(')[1]
                coords = coords.split(',')
                coords = [float(coord) for coord in coords]
                score = data[1]
                score = float(score.split('=')[1])

                points.append(coords)
                scores.append(score)

            points = np.array(points)
            x = points[:, 0]
            y = -points[:, 1]

            x_cm = np.mean(x)
            y_cm = np.mean(y)

            # center by the average
            x = x - x_cm
            y = y - y_cm


            plt.scatter(x, y)
            plt.xlim(-.5, .5)
            plt.ylim(-.5, .5)
            plt.gca().set_aspect('equal')
            plt.pause(1e-9)
