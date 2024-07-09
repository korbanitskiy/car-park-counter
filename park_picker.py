import cv2
import json

width, height = 107, 48
color = (255, 0, 255)
thickness = 2


class JSONParkPicker:

    def add(self, x: int, y: int):
        pass

    def remove(self, x: int, y: int):
        pass
        # for i, position in enumerate(positions):
        #     x1, y1 = position
        #     if (x1 < x < x1 + width) and (y1 < y < y + height):
        #         positions.pop(i)

    def save(self):
        pass

    def __call__(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            self.add(x, y)
    
        if events == cv2.EVENT_RBUTTONDOWN:
            self.remove(x, y)
    

def select_positions():
    picker = JSONParkPicker("parks")
    while True:
        img = cv2.imread("carParkImg.png")
        for park in picker.parks:
            cv2.rectangle(img, park, (park[0] + width, park[1] + height), color, thickness)

        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", picker)
        cv2.waitKey(1)


if __name__ == "__main__":
    select_positions()


