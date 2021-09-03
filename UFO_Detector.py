#Developed By 1803357 (regnumber)
#CE316 Assignment 1

"""
Purpose of this Program
    - This program can be used by astronomers/scientists to help determine whether they have identified a meteor or a UFO
    - The program idenitifies the colour of an identity/object and determines if it is travelling in a straight line or is changing trajectories
"""

"""
The Structure of my Code
1. Functions:
    - Have created two functions called "get_mid_points" and "distance"
    - The functions have been created as they need to be run for each identity/colour that is detected
    - This reduces the need for duplicate code

2. Colour Detection:
    - The colours detected are Blue, Cyan, Green, Yellow, Orange, Red and White
    - An additional colour (Black) is also identified in the function "get_mid_points", which is classed as the background

3. Algorithm:
    - To start with, my definitions are declared
    - The left and right frames are then read in order of frame number. Only the number of frames specified in the terminal will be read
    - Converting to greyscale is not required as OpenCV will automatically do this
    - A template for generating the filename for the left-hand frames is applied
    - A template for generating the filename for the right-hand frames is applied
    - Using the function "get_mid_points", the mid-point is calculated and recorded for each identity/colour in a left-hand frame
    - Using the function "get_mid_points", the mid-point is calculated and recorded for each identity/colour in a right-hand frame
    - The distance of each identity/colour is calculated using the function "distance"
    - Distance results are then printed in the format required
    - The angle change for each object is then calculated
    - The object which changes trajectory (angle) the most is recorded as the UFO
    - The UFO's identity/colour is then printed

4. Algorithm Justification
    - The total time for execution of the program, for 50 frames, is 3 minutes 24 seconds, which is 4.1 seconds per frame.
        I have optimised the code by using functions
    - I have used the algotrithm mentioned in the above section, as it enables me to execute the program with a single command:
        'python3 ce316ass.py 50 left-%3.3d.png right-%3.3d.png'
    - It uses the function called "get_mid_points" and "distance" to reduce repetition of code
    - The function "get_mid_points" is used as midpoint helps provide more accuracy in finding an objects location rather than looking at its contour.
    - The greatest angle change of an object identifies if it is a UFO, an object that is not travelling in a straight line.
        If it travels in a straight line it is a meteor
    - I believe that the right alogrithm has been selected as the expected result is produced

5. Coding Style
    - I have used variable/fucntion names that are easy to understand e.g. the function "get_mid_points" is self explanatory
    - Have provided easy to read comments at the beginning of each section of code
    - Have used two types of comments: block and single line comments
    - Code Maintanence
        * To provide the ability of code maintanence, I have produced two functions which can be changed easily,
            without having to change the code for each individual colour
        * I have also produced individual identity/colour result printing, in order to make easy colour changes
    - For reusability of code, I have used functions/modules
    - Have used standard procedures by importing, defining my own functions and then coding the main program
    - Kept memory usage in perspective, hence have only stored necessary data and it is called only when required e.g. identities detected in each frame
    - Have arranged data carefully, so as to not repeat calculations e.g. for the UFO calculation, the angle is only being compared to the angle in the last frame

6. Results
    - The program can be invoked as per the specification on Page 2 of the Assignment Brief i.e. python3 ce316ass.py 50 left-%3.3d.png right-%3.3d.png
    - An error message is produced when the correct input is not entered into the terminal window. It also suggests the correct input style
    - Distance results are printed with 2 decimal places and are also in standard form
    - As I have been developing the program, have executed the program multiple times and removed all identified bugs
    - Running the program:
        * Input requires the left and right frames. User can specify the number of frames by replacing 50 in the command:

                python3 ce316ass.py 50 left-%3.3d.png right-%3.3d.png

        * Output would be in the following format, as shown by the example below mentioned on Page 3 of the Assignment Brief:

            frame  identity   distance
        ...
            12   red        1.71e+12
            12   yellow     1.62e+12
        ...
            UFO: cyan

    - I have reverified that the results match the format specified in the Assignment Brief

7. Presentation
    - I have used comments all through-out the program in the format of block and single line comments
    - A person maintaining the code should easily be able to understand how and where to make changes
    - The purpose of this program is mentioned at the start of this file on Line 5
    - In Python programming, indentation is required or else the program will not work
    - Have conformed to the house-style by ensuring that no line of code is longer than 80 characters. Longer lines have been split into the next line.
        However comments are over 80 characters so they are easy to read
    - Blank lines have been included to aid the reader's understanding
    - White spaces within lines have been used to make them easier to read
"""

#Start of Code

#-----------------------------------------------------------------------------
#Import all necessary modules
#-----------------------------------------------------------------------------

#The sys library provides variables needed and maintianed by the interpreter
import sys
#The cv2 library is needed for the Computer Vision aspect of the program i.e image processing
import cv2
#The math library provides access to common math functions i.e. angle calculation
import math


#Focal Length (fixed value) provided in Assignment Brief
FOCAL_LENGTH = 12
#Distance between cameras in meters (fixed value), provided in Assignment Brief
DISTANCE = 3500

#-----------------------------------------------------------------------------
#The following function identifies the bright coloured pixels for an object and calculates their midpoint
#-----------------------------------------------------------------------------

def get_mid_points(im):
    # The respective frames width and height are stored
    im_h = im.shape[0]
    im_w = im.shape[1]

    #Initialising xlo,xhi and ylo,yhi values
    xlo = im_w + 1
    xhi = -1
    ylo = im_h + 1
    yhi = -1

    #Each colour's mid-point is set to (0,0) at the start
    red=[0,0,0,0]
    blue=[0,0,0,0]
    cyan=[0,0,0,0]
    green=[0,0,0,0]
    orange=[0,0,0,0]
    yellow=[0,0,0,0]
    white=[0,0,0,0]

#-----------------------------------------------------------------------------
    """
    - The following code is used to differentiate between objects and the background
    - The following loop logic was obtained from Slide 3 and Slide 4 of 'Topic 2 - Getting started with OpenCV' on Moodle
    - Similar code to the loop was provided by Prof. Adrian Clark via email on 7/3/21
    """
#-----------------------------------------------------------------------------

    for y in range(0,im_h):
        for x in range(0,im_w):
            #Get blue, green, red values of each pixel
            b,g,r = im[y,x]

            #Check if the pixel is black
            if r==0 and g==0 and b==0:
                continue


            #Check if the pixel is red
            elif r>0 and g==0 and b==0:
                im[y,x] = (0,0,255)
                if x < xlo:
                    red[0] = x
                if x > xhi:
                    red[1] = x
                if y < ylo:
                    red[2] = y
                if y > yhi:
                    red[3] = y

            #Check if the pixel is orange
            elif r>0 and g<190 and b==0:
                im[y,x] = (0,170,255)
                if x < xlo:
                    orange[0] = x
                if x > xhi:
                    orange[1] = x
                if y < ylo:
                    orange[2] = y
                if y > yhi:
                    orange[3] = y

            #Check if the pixel is yellow
            elif r>0 and g>0 and b==0:
                im[y,x] = (0,255,255)
                if x < xlo:
                    yellow[0] = x
                if x > xhi:
                    yellow[1] = x
                if y < ylo:
                    yellow[2] = y
                if y > yhi:
                    yellow[3] = y

            #Check if the pixel is blue
            elif r==0 and g==0 and b>0:
                im[y,x] = (255,0,0)
                if x < xlo:
                    blue[0] = x
                if x > xhi:
                    blue[1] = x
                if y < ylo:
                    blue[2] = y
                if y > yhi:
                    blue[3] = y

            #Check if the pixel is cyan
            elif r==0 and g==b:
                im[y,x] = (175,175,0)
                if x < xlo:
                    cyan[0] = x
                if x > xhi:
                    cyan[1] = x
                if y < ylo:
                    cyan[2] = y
                if y > yhi:
                    cyan[3] = y

            #Check if the pixel is green
            elif r==0 and g>0 and b==0:
                im[y,x] = (0,255,0)
                if x < xlo:
                    green[0] = x
                if x > xhi:
                    green[1] = x
                if y < ylo:
                    green[2] = y
                if y > yhi:
                    green[3] = y

            #Check if the pixel is white
            elif r>0 and g>0 and b>0:
                im[y,x] = (255,255,255)
                if x < xlo:
                    white[0] = x
                if x > xhi:
                    white[1] = x
                if y < ylo:
                    white[2] = y
                if y > yhi:
                    white[3] = y

    #The stored midpoints are returned
    return ((blue[0]+blue[1])//2,(cyan[0]+cyan[1])//2 ,(green[0]+green[1])//2 ,
                (yellow[0]+yellow[1])//2,(orange[0]+orange[1])//2,
                (red[0]+red[1])//2 , (white[0]+white[1])//2 ,

            (blue[2]+blue[3])//2,(cyan[2]+cyan[3])//2 ,(green[2]+green[3])//2 ,
                (yellow[2]+yellow[3])//2,(orange[2]+orange[3])//2,
                (red[2]+red[3])//2 , (white[2]+white[3])//2 )


#-----------------------------------------------------------------------------
# A function to calculate an objects distance from Earth
#-----------------------------------------------------------------------------

def distance(xmid_l,xmid_r):
    global FOCAL_LENGTH,DISTANCE
    return (FOCAL_LENGTH*DISTANCE)/(float(xmid_l)*0.00001-float(xmid_r*0.00001))


#-----------------------------------------------------------------------------
#Checks if input is entered correctly
#-----------------------------------------------------------------------------

if(not len(sys.argv)==4):
    print("Please enter the correct input to run the program")
    print("Use the following format:")
    print(" %s <frames> <filename-left> <filename-right>"% sys.argv[0],
file=sys.stderr)
    exit(1)


#Getting number of frames from terminal input
#Obtained from Page 2 of the Assignment Brief
no_frames = int (sys.argv[1])


#-----------------------------------------------------------------------------
#Print column headings and "..." as required in the Assignment Brief
#-----------------------------------------------------------------------------

print("frame     identity     distance")
print("...")


#Declares the angle variables for each colour and sets them to 0
red_p_angle=0
red_c_angle=0
white_p_angle=0
white_c_angle=0
cyan_p_angle=0
cyan_c_angle=0
yellow_p_angle=0
yellow_c_angle=0
orange_p_angle=0
orange_c_angle=0
blue_p_angle=0
blue_c_angle=0
green_p_angle=0
green_c_angle=0
ufo = []


#-----------------------------------------------------------------------------
"""
The following lines of code are used for
    1. The number of frames to be processed
    2. A template for generating the filename of a left-hand frame
    3. A template for generating the filename of a right-hand frame

Part of this code was provided on Page 2 of the Assignment Brief
"""
#-----------------------------------------------------------------------------

for frame in range(0,no_frames):
    #Converting frame numbers to filenames
    fn_left = sys.argv[2] % frame
    fn_right = sys.argv[3] % frame

    #Read frames left then right
    im_left = cv2.imread(fn_left,cv2.IMREAD_COLOR)
    im_right = cv2.imread(fn_right,cv2.IMREAD_COLOR)

    #Objects midpoints are called from the 'get_mid_points' function
    (blue_xmid_l,cyan_xmid_l,green_xmid_l,yellow_xmid_l,orange_xmid_l,
red_xmid_l,white_xmid_l,blue_ymid_l,cyan_ymid_l,green_ymid_l,yellow_ymid_l,
orange_ymid_l,red_ymid_l,white_ymid_l) = get_mid_points(im_left)

    (blue_xmid_r,cyan_xmid_r,green_xmid_r,yellow_xmid_r,orange_xmid_r,
red_xmid_r,white_xmid_r,blue_ymid_r,cyan_ymid_r,green_ymid_r,yellow_ymid_r,
orange_ymid_r,red_ymid_r,white_ymid_r) = get_mid_points(im_right)


#-----------------------------------------------------------------------------
    """
    Try loop which:
        1. Calculates Distance using the function 'distance'
        2. Prints each objects result

    To print in standard form, the following website was used:
        https://www.w3schools.com/python/ref_func_format.asp
    """
#-----------------------------------------------------------------------------

    try:
        print("  " +str(frame) + "        " +"Blue" + "         " +str("{:.3g}"
.format(distance(blue_xmid_l,blue_xmid_r))) )
        print("  " +str(frame) + "        " +"Cyan" + "         " +str("{:.3g}"
.format(distance(cyan_xmid_l,cyan_xmid_r),".2f")) )
        print("  " +str(frame) + "        " +"Green" + "        " +str("{:.3g}"
.format(distance(green_xmid_l,green_xmid_r),".2f")) )
        print("  " +str(frame) + "        " +"Yellow" + "       " +str("{:.3g}"
.format(distance(yellow_xmid_l,yellow_xmid_r),".2f")) )
        print("  " +str(frame) + "        " +"Orange" + "       " +str("{:.3g}"
.format(distance(orange_xmid_l,orange_xmid_r),".2f")) )
        print("  " +str(frame) + "        " +"Red" + "          " +str("{:.3g}"
.format(distance(red_xmid_l,red_xmid_r),".2f")) )
        print("  " +str(frame) + "        " +"White" + "        " +str("{:.3g}"
.format(distance(white_xmid_l,white_xmid_r),".2f")) )


#-----------------------------------------------------------------------------
        """
        The following code is used to record the 3D position of each object via angle
        change and try to establish which are and which are not, travelling in straight lines.

        Those not travelling in a straight line is/are the UFO(s)
        """
#-----------------------------------------------------------------------------

        blue_c_angle = cv2.fastAtan2(blue_ymid_l,blue_xmid_l)
        cyan_c_angle = cv2.fastAtan2(cyan_ymid_l,cyan_xmid_l)
        green_c_angle = cv2.fastAtan2(green_ymid_l,green_xmid_l)
        yellow_c_angle = cv2.fastAtan2(yellow_ymid_l,yellow_xmid_l)
        orange_c_angle = cv2.fastAtan2(orange_ymid_l,orange_xmid_l)
        red_c_angle = cv2.fastAtan2(red_ymid_l,red_xmid_l)
        white_c_angle = cv2.fastAtan2(white_ymid_l,white_xmid_l)


#-----------------------------------------------------------------------------
    #If/elif loop is used to compare the previous angle of an object to its current angle
    #If there is a change in angle, the object is identified as a UFO
#-----------------------------------------------------------------------------

    except ZeroDivisionError:
        pass
    print("...")
    #Check if theres is a big angle change
    if "Blue" in ufo:
        pass
    else:
        if blue_p_angle-blue_c_angle > 6:
            ufo.append("Blue")
    if "Cyan" in ufo:
        pass
    else:
        if cyan_p_angle-cyan_c_angle > 6:
            ufo.append("Cyan")
    if "Green" in ufo:
        pass
    else:
        if green_p_angle-green_c_angle > 6:
            ufo.append("Green")
    if "Yellow" in ufo:
        pass
    else:
        if yellow_p_angle-yellow_c_angle > 6:
            ufo.append("Yellow")

    if "Orange" in ufo:
        pass
    else:
        if orange_p_angle-orange_c_angle > 6:
            ufo.append("Orange")
    if "Red" in ufo:
        pass
    else:
        if red_p_angle-red_c_angle > 6:
            ufo.append("Red")
            print("red in")
    if "White" in ufo:
        pass
    else:
        if white_p_angle-white_c_angle > 6:
            ufo.append("White")
            print("white in")

    #Current angles are turned into previous angles to be checked for next frame
    blue_p_angle = blue_c_angle
    cyan_p_angle = cyan_c_angle
    green_p_angle = green_c_angle
    yellow_p_angle = yellow_c_angle
    orange_p_angle = orange_c_angle
    red_p_angle = red_c_angle
    white_p_angle = white_c_angle

#Used to print the object stored in 'ufo'
print("UFO:" + str(ufo))


"""
 DEBUG = false
   ...
   if DEBUG:
      print ("xlo and xhi for the red object:", xlo, xhi)
      cv2.imshow ("Red", im)
"""
