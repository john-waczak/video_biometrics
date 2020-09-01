import numpy as np
import matplotlib.pyplot
import pandas as pd
from tqdm import tqdm
import cv2


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


def getLandmarks(pic):
    image = cv2.imread(pic)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Detect faces using the haarcascade classifier on the "grayscale image"
    faces = detector.detectMultiScale(image_gray)
    if len(faces) > 0:
        _, landmarks = landmark_detector.fit(image_gray, faces)
        # scale by the height
        (x,y,w,h) = faces[0]
        return (landmarks[0]/h).tolist()[0]
    else:
        return []

