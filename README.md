# WebcamMotionDetector

A simple script written in Python using OpenCV, pandas and Bokeh. The script opens the computer's webcam and saves the first frame as an image. Subsequently it records video and compares
any changes from each frame with the first image and comparing it to some threshold level, thus detecting 'motion'. The image is filtered using a Gaussian blur. Any motion that is detected
is recorded using date-time features and upon termination of the script, a plot is shown indicating times when motion was detected.
