import picamera
import io


CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def Capture():
    camera.capture('image.jpg')
    data = open("image.jpg","rb")
    return data

if __name__ == "__main__":
    Capture()