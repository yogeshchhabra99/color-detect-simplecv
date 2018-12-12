# color-detect-simplecv
This is one of my first programs using SimpleCV.
Run the python script, it takes an image of 480*640 pixels, crops a square of 200,200 at 200,200 pixel
(note that the origin is the top left corner)
It finds the meancolor in the cropped image
This process is in an infinite loop with a timedelay of 1 second
To install SimpleCV in Ubuntu, follow
      https://junise.wordpress.com/2016/01/17/installing-simplecv-in-ubuntu/
Note that the output format is (B,R,G).
