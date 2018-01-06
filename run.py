import picamera
import socket
import io

# Code for CitySynth project
#
# Let's hope this works. If it's successful, yay. If not, we're screwed. Probably.
#
frames = 0
'''
print("Connecting to socket.")
socket_stream = socket.socket() 
socket_stream.connect(('localhost',8000))
sconnect = socket_stream.makefile('wb')
print("Connection has finished")
'''
class Camera:
    def __init__(self):
          self.camera = picamera.PiCamera()
          self.camera.resolution = (1080,768)
          self.camera.start_preview()
    def begin_stream(self):
	global frames
        stream = io.BytesIO()
        for i in self.camera.capture_continuous(stream,'jpeg'):
		frames += 1
		print(frames)
'''
            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent

            sconnect.write(struct.pack('<L', stream.tell()))
            sconnect.flush()

            # Rewind the stream and send the image data over the wire

            stream.seek(0)
            sconnect.write(stream.read())

            # Reset the stream for the next capture

            stream.seek(0)
            stream.truncate()
            connection.write(struct.pack('<L', 0))
'''
cam = Camera()
cam.begin_stream()
