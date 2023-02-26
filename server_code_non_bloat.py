 1   # run this program on the Mac to display image streams from multiple RPis
 2   import cv2
 3   import imagezmq
 4   image_hub = imagezmq.ImageHub()
 5   while True:  # show streamed images until Ctrl-C
 6       rpi_name, image = image_hub.recv_image()
 7       cv2.imshow(rpi_name, image) # 1 window for each RPi
 8       cv2.waitKey(1)
 9       image_hub.send_reply(b'OK')
