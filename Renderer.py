import numpy
import Colors
import PIL, PIL.ImageDraw, PIL.ImageFont

size = (_, height) = 64, 64
font = PIL.ImageFont.truetype('Fonts/FiraCode.ttf', 32)

def render(character: str) -> numpy.ndarray:
    image = PIL.Image.new('1', size, Colors.white)

    canvas = PIL.ImageDraw.Draw(image)
    canvas.text((0, 0), character, Colors.black, font)

    image.save(f'{character}.png')

    return numpy.array(image.getdata()).reshape(size[::-1])