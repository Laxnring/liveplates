# liveplates
Live camera feed license plate detector, based on OpenALPR.

This repo contains the standard OpenALPR build for Windows and the installed Python binding. 
As the [current OpenALPR release](https://github.com/openalpr/openalpr/releases) doesn't work out of the box with Python, some of the 
code related to the porting script (openaclr.py) was rewritten to be Python 3.7 compatible and run out-of-the-box.

This repo also features a practical implementation of the script (detection.py) to create a live video stream using 
[OpenCV](https://github.com/opencv/opencv) and detect license plates as the stream is generated. While a given license plate
is being detected, it's confidence values are summed and the most likely license plate number is registered and displayed as 
command line output of the stream. 

# Running the script:

Running from the repo base directory: 
`python ./detection.py`

# Required dependencies
The camera livestream requires OpenCV to be installed on the system. 
