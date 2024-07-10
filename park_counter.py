import cv2
import cvzone
import numpy as np
from park_picker import JSONPicker, WIDTH, HEIGHT, COLOR, THICKNESS, ParkSpace


def check_parking_spaces(img, park_spaces: list[ParkSpace]):
    for space in park_spaces:
        img_crop = img[space.y: space.y + HEIGHT, space.x: space.x + WIDTH]
        cv2.imshow(str(space.y*space.x), img_crop)




def count_park_spaces():
    picker = JSONPicker("park_spaces.json")
    park_spaces = picker.load_current_spaces()
    cap = cv2.VideoCapture("carPark.mp4")
    
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


        success, img = cap.read()
        check_parking_spaces(img, park_spaces)
        for space in park_spaces:
            cv2.rectangle(img, (space.x, space.y), (space.x + WIDTH, space.y + HEIGHT), COLOR, THICKNESS)


        cv2.imshow("Image", img)
        cv2.waitKey(10)





if __name__ == "__main__":
    count_park_spaces()