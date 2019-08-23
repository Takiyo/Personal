from PIL import Image
import random, time
im = Image.open('gradienttest.png')
im.save('dither.png')
out = Image.open('dither.png')
print(out.format, out.size, out.width, out.height)


def RGBstatic():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def randomdither(pix):
    rand = random.randint(0, 765)
    r = pix[0]
    g = pix[1]
    b = pix[2]
    alpha = pix[3]
    a = r + g + b
    if alpha < 50:
        return (255, 255, 255, 0)
    if a < 20:
        return (0, 0, 0)
    if a > rand or a > 650:
        return (255, 255, 255, 0)

    else:
        return (0, 0, 0)


def rgb(pix, rgb):
    if pix == 0:
        return 0
    r = pix[0]
    g = pix[1]
    b = pix[2]
    if rgb == 'red':
        return r
    elif rgb == 'green':
        return g
    else:
        return b

def index(x, y):
    return x + (y * out.width)

imag = list(im.getdata())

#randomimage = []

for y in range(0, out.height-1):
    for x in range(1, out.width-1):
        pixel = imag[index(x,y)]
        # (255, 255, 255)
        # oldR = rgb(pixel, 'red')
        # oldG = rgb(pixel, 'green')
        # oldB = rgb(pixel, 'blue')
        oldR = pixel[0]
        oldG = pixel[1]
        oldB = pixel[2]

        factor = 7

        newR = int(round(factor * oldR / 255) * (255/factor))
        newG = int(round(factor * oldG / 255) * (255/factor))
        newB = int(round(factor * oldB / 255) * (255/factor))

        imag[index(x,y)] = (newR, newG, newB)

        errR = oldR - newR
        errG = oldG - newG
        errB = oldB - newB

        c = imag[index(x+1, y)]
        r = rgb(c, 'red')
        g = rgb(c, 'green')
        b = rgb(c, 'blue')
        r = int(r + errR * 7/16)
        g = int(g + errG * 7/16)
        b = int(b + errB * 7/16)
        imag[index(x+1, y)] = (r, g, b)

        c = imag[index(x-1, y+1)]
        r = rgb(c, 'red')
        g = rgb(c, 'green')
        b = rgb(c, 'blue')
        r = int(r + errR * 3/16)
        g = int(g + errG * 3/16)
        b = int(b + errB * 3/16)
        imag[index(x-1, y+1)] = (r, g, b)

        c = imag[index(x, y+1)]
        r = rgb(c, 'red')
        g = rgb(c, 'green')
        b = rgb(c, 'blue')
        r = int(r + errR * 5/16)
        g = int(g + errG * 5/16)
        b = int(b + errB * 5/16)
        imag[index(x, y+1)] = (r, g, b)

        c = imag[index(x+1, y+1)]
        r = rgb(c, 'red')
        g = rgb(c, 'green')
        b = rgb(c, 'blue')
        r = int(r + errR * 1/16)
        g = int(g + errG * 1/16)
        b = int(b + errB * 1/16)
        imag[index(x+1, y+1)] = (r, g, b)

        #randomimage.append((newR, newG, newB))

out.putdata(imag)
out.save('floydoutput.png')
print("done")


