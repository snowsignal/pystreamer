import socket
import sys
import subprocess

host = sys.argv[1]
server_socket = socket.socket()
server_socket.connect((host, 8000))
print("Connected to " + host)

connection = server_socket.makefile('rb')
try:
    # Run VLC using the MJPEG codec
    cmdline = ['vlc', '--demux', 'mjpeg', '-']
    player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
    while True:
        data = connection.read(1024)
        if not data:
            break
        player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    player.terminate()
