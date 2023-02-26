# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

# construct the argument parser and parse the arguments. Need server IP.
ap = argparse.ArgumentParser()
ap.add_argument("-s", -i"--serverp", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
	args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
vs = VideoStream(usePiCamera=False).start()
# Get stream from webcam and set parameters)
#vs = VideoStream(src=0).start()//source set to what the file is written to i guess. temp mem buffer.
#vs = VideoStream(src=0, resolution=(320, 240)).start()//other one
time.sleep(2.0)

while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	sender.send_image(rpiName, frame)





