import numpy
import opennsfw2
from PIL import Image

from roop.typing import Frame

MAX_PROBABILITY = 0.85

PREDICTOR = None

def clear_predictor() -> None:
    global PREDICTOR
    PREDICTOR = None


def predict_frame(target_frame: Frame) -> bool:
    return False


def predict_image(target_path: str) -> bool:
    return False


def predict_video(target_path: str) -> bool:
    return False
