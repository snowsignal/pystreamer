import socket
import time
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.bind(('', 8000))
client_socket.listen(0)
# Make a file-like object out of the connection
connection = client_socket.accept()[0].makefile('wb')
print("Connection establised")
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
        # Start a preview and let the camera warm up for 2 seconds
        time.sleep(2)
        # Start recording, sending the output to the connection for 60
        # seconds, then stop
	camera.start_preview()
        camera.start_recording(connection, format='mjpeg')
	while 1:
		pass
        camera.stop_recording()
finally:
    connection.close()
    client_socket.close()
