# mjpeg_stream_tests
A server and a client in python for mjpeg streams for testing

# You will need
For the test server:

     sudo apt-get install gstreamer-tools

Python lib for the example viewer
(I had them already in my machine so it may need more work than this commands)

     sudo pip install cv2
     sudo pip install numpy


# Run the server
One terminal:

    python mjpeg_test_server.py

Note: sometimes it hangs when you Control+C it, just kill it, you can do Control+Z (send to background) and `kill -9 %%` (kill background process).

Another terminal:

    gst-launch videotestsrc pattern=ball ! video/x-raw-rgb, framerate=15/1, width=640, height=480 !  jpegenc ! multipartmux boundary=spionisto ! tcpclientsink port=9999

# Run the viewer

   python view_mjpeg_stream.py

You can also view the stream with firefox (it has a player predefined) opening the url:

http://localhost:1337/mjpeg_stream

You should see something like this:

![Screenshot of the stream and the viewer working](https://raw.githubusercontent.com/awesomebytes/gazebo_ros_light/master/working_screenshot.png)


Tested with an ipcam and a video stream from the ROS package web_video_server from a simulated robot.
