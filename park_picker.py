import json
import os
from typing import NamedTuple

import cv2  # type: ignore

WIDTH, HEIGHT = 107, 48
COLOR = (255, 0, 255)
THICKNESS = 2


class ParkSpace(NamedTuple):
    x: int
    y: int


class JSONPicker:

    def __init__(self, path: str) -> None:
        self.path = path
        self._spaces: list[ParkSpace] = []

    def add(self, x: int, y: int):
        self._spaces.append(ParkSpace(x, y))

    def remove(self, x: int, y: int):
        for i, space in enumerate(self._spaces):
            x_inside = x in range(space.x, space.x + WIDTH)
            y_inside = y in range(space.y, space.y + HEIGHT)
            if x_inside and y_inside:
                self._spaces.pop(i)
                break

    def save(self):
        with open(self.path, "w") as fp:
            json.dump(self._spaces, fp, indent=2)

    @property
    def spaces(self) -> list[ParkSpace]:
        return self._spaces

    def __call__(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            self.add(x, y)

        if events == cv2.EVENT_RBUTTONDOWN:
            self.remove(x, y)

    def __enter__(self):
        self._spaces = self._load_current_spaces()
        return self

    def __exit__(self, exc, exc_type, exc_val):
        self.save()

    def _load_current_spaces(self) -> list[ParkSpace]:
        if not os.path.exists(self.path):
            return []

        with open(self.path) as fp:
            return [ParkSpace(row[0], row[1]) for row in json.load(fp)]


def select_positions():
    with JSONPicker("park_spaces.json") as picker:
        while True:
            img = cv2.imread("carParkImg.png")
            for space in picker.spaces:
                cv2.rectangle(img, (space.x, space.y), (space.x + WIDTH, space.y + HEIGHT), COLOR, THICKNESS)

            cv2.imshow("Image", img)
            cv2.setMouseCallback("Image", picker)
            cv2.waitKey(1)


if __name__ == "__main__":
    select_positions()
