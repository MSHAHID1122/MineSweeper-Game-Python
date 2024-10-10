from . import setting


def height_percnt(percentage: int):
    return (percentage/100) * setting.HEIGHT

def width_percnt(percentage: int):
    return (percentage/100) * setting.WIDTH
