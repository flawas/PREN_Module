import os, sys, logging, time
from waveshare_epd import epd1in54_V2
from PIL import Image, ImageDraw, ImageFont

def __init__(epd, fontTTC, backgroundBMP ):
    logging.info("Display init")
    font = ImageFont.truetype(os.path.join(fontTTC), 16)
    epd.init(1)
    background = Image.open(os.path.join(backgroundBMP))
    epd.displayPartBaseImage(epd.getbuffer(background))

    # epd.init(1) # into partial refresh mode
    ImageDraw.Draw(background)

def clearDisplay(epd):
    logging.info("Display clear")
    try:
        epd.init(0)
        epd.Clear(0xFF)
        epd.init(1)
        time.sleep(1)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def drawPicture(epd, picture):
    logging.info("Display draw picture")
    try:
        epd.init(0)
        image = Image.open(os.path.join(picture))
        epd.display(epd.getbuffer(image))
        time.sleep(15)

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def shutdownDisplay(epd):
    logging.info("Display shutdown")
    epd.init(0)
    epd.Clear(0xFF)
    epd.sleep()

def drawInitialDisplay(epd, background):
    logging.info("Display draw initial display")
    try:
        epd.init(1)
        updateDisplay(epd, 10, 10, 'PREN TEAM 33', backgroundBMP=background)
        # self.updateDisplay(10, 30, 'Initialisierung')
        updateDisplay(epd, 10, 80, 'Beanspruchte Zeit', backgroundBMP=background)
        # self.updateDisplay(10, 100, 'Sekunden')
        updateDisplay(epd, 10, 150, 'Stromverbrauch', backgroundBMP=background)
        # self.updateDisplay(10, 170, 'kW')

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def updateDisplay(epd, x, y, text, backgroundBMP):
    logging.info("Display update: x:" + str(x) + ", y: " + str(y) + ", text: " + str(text))
    try:
        image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        epd.init(1)
        background = Image.open(backgroundBMP)

        draw = ImageDraw.Draw(image)
        draw.rectangle((x, y, 200, y + 20), fill=0)
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        draw.rectangle((x, y, 200, y + 20), fill=(255, 255, 255))
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        draw.text((x, y), text, fill=0)
        newimage = background.crop([x, y, 200, y + 20])

        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        background.save("background_modified.png")

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def loop(self):
    self.drawPicture('qrcode.bmp')
    self.clearDisplay()
