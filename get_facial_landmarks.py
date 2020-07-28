import numpy as np
from glob import glob
import re
import json
from tqdm import tqdm
# opencv 4.1.2 to read images
import cv2

# get frames
path_to_frames = './frames/'
fps = 15  # determined by ffmpeg


# load in face detector -------------------------------------------------
haarcascade = "./haarcascade_frontalface_alt2.xml"
# create an instance of the Face Detection Cascade Classifier
detector = cv2.CascadeClassifier(haarcascade)


# load in facial landmark detector --------------------------------------

LBFmodel = "./lbfmodel.yaml"
# create an instance of the Facial landmark Detector with the model
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel(LBFmodel)

# -----------------------------------------------------------------------


output = {}
i = 0

# sort them into the correct order
files = glob(path_to_frames+'*.png')
files.sort(key=lambda f: int(re.sub('\D', '', f)))
print('Sorted {} files.'.format(len(files)))
for pic in tqdm(files):
    # read image with openCV
    image = cv2.imread(pic)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # convert to grayscale 
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Detect faces using the haarcascade classifier on the "grayscale image"
    detected = {}
    detected["dimensions"] = []
    faces = detector.detectMultiScale(image_gray)
    if len(faces) > 0:
        _, landmarks = landmark_detector.fit(image_gray, faces)
        for j in range(len(landmarks)):
            # scale by the height
            (x,y,w,h) = faces[j]
            detected[j] = (landmarks[j]/h).tolist()

    output[i] = detected
    i += 1

with open('landmarks.json', 'w') as fp:
    json.dump(output, fp)

