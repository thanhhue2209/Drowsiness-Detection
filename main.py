import cv2
import mediapipe
import numpy as np
from model import *
import queue_check
import time
import pygame
pygame.init()

start_point = (5,5)
end_point = (635, 475)
thickness = 2
camera = cv2.VideoCapture(0)
pTime = 0
mpDraw = mediapipe.solutions.drawing_utils
mpFaceMesh = mediapipe.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
eyes_left = np.zeros((100, 100, 3), np.uint8)
eyes_right = np.zeros((100, 100, 3), np.uint8)
model = prepare_model()
q = queue_check.queue(5)

while True:
    eyes = []
    _, img = camera.read()
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRBG)
    land_marks = {}

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            # mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS,
            # drawSpec,drawSpec)
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                if id == 46 or id == 174 or id == 285 or id == 340:
                    land_marks[id] = [x, y]
        try:
            eyes_left = img[land_marks[46][1]:land_marks[174][1], land_marks[46][0]:land_marks[174][0]].copy()
            eyes_right = img[land_marks[285][1]:land_marks[340][1], land_marks[285][0]:land_marks[340][0]].copy()
            eyes.extend([eyes_right, eyes_left])
            res = pipeline_predict(model, eyes)
            q.push(res)
            if q.check() == 0:
                print("Nguy Hiem")
                cv2.rectangle(img, start_point, end_point, (0,0,255), thickness)
                cv2.putText(img, "Nguy Hiem", (20, 70), cv2.FONT_HERSHEY_PLAIN,
                            3, (0, 0, 255), 3)
                music = pygame.mixer.Sound('sound_.mp3')
                music.play()
            else:
                print("An Toan")
                cv2.rectangle(img, start_point, end_point, (0,255,0), thickness)

                cv2.putText(img, "An Toan", (20, 70), cv2.FONT_HERSHEY_PLAIN,
                            3, (0, 255, 0), 3)
        except Exception as e:
            print(e)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                #3, (0, 255, 0), 3)

    cv2.imshow("", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

