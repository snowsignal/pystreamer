# PyStreamer
A python-based streaming script for the Raspberry Pi

PyStreamer was created by Jackson Lewis ([@JacksonCoder](https://github.com/Jacksoncoder)) for the CitySynth project. This project includes code for both the server and the client
to use. The server code should be run on a Raspberry Pi, while the client code can be run on any device that has VLC and Python installed.

## Getting Started

### Raspberry Pi

#### Setting up the Raspberry Pi
Before we can run the server code on the Pi, we need to install a few things.

First, run `sudo apt-get update` and `sudo apt-get upgrade` to get the latest packages for your system.

Then, install the nessecary dependencies from Pip (in this case, only one package): `pip install picamera`

Then, `git clone` the project: `git clone https://github.com/JacksonCoder/pystreamer`

#### Running the camera server
Go to the directory where this project is installed, and then run `python camera_server.py`. Wait a few seconds, and you should
see the video previewed on your screen. The server is up and running! Unfortunately, it still isn't connected to any client programs
yet. You'll have to install PyStreamer on another computer to do that.

### The viewing computer

#### Setting up the viewing computer
First, make sure you have VLC and Python installed on this computer. Once that requirement is fulfilled, `git clone` the project:
`git clone https://github.com/JacksonCoder/pystreamer`

Before you can run this, you also need to obtain the IP address of the Raspberry Pi. Run `ifconfig` on the Pi to get it's IP address.
You will need it for the next step. Also make sure you are on the same network as the Pi.

#### Running the viewer
First, go to the directory where you have installed the project. Make sure the Pi is running the server script.

Once you have done that, run this command: `python stream_viewer.py <your-raspberry-pi-ip>`, using the IP address you obtained 
earlier.

Wait a few seconds, and then VLC should start displaying the streamed video on the viewing computer's screen. You might see a 1 to 2
second delay between the preview and the streamed video; this is normal.


If you have any questions or run into any problems, feel free to open a Github Issue, or contact the author via email at
`st.japa6@gmail.com`.
