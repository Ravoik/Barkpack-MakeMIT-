 1   # run this program on each RPi to send a labelled image stream
 2   import socket
 3   import time
 4   from imutils.video import VideoStream
 5   import imagezmq
 6
 7   sender = imagezmq.ImageSender(connect_to='tcp://jeff-macbook:5555')
 8
 9   rpi_name = socket.gethostname() # send RPi hostname with each image
10   picam = VideoStream(src=0).start()
11   time.sleep(2.0)  # allow camera sensor to warm up
12   while True:  # send images as stream until Ctrl-C
13       image = picam.read()
14       sender.send_image(rpi_name, image)

#vs = VideoStream(src=0).start()//source set to what the file is written to i guess. temp mem buffer.
#vs = VideoStream(src=0, resolution=(320, 240)).start()#//other one, not certain if it works

