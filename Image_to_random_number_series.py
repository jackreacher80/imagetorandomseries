"""
File: image_to_random_number_series.py
----------------
This program converts images to a random number series. It uses signals like timestamp and randint output to generate randomness and then
uses the LCG algorithm to generate a random series.

It then plots a graph of every pixel against the random number generated. Every pixel value
generates adds more randomness to the series
"""

DEFAULT_FILE = 'images/simba-sq.jpg'


import time
import random
import imagerandom
from simpleimage import SimpleImage

def main():
    """This is how we generate the seed or the first terms Xn of the random series"""
    seed = time.time() * random.randint(0, 1000)
    print("The seed or first term of the series Xn is= " + str(seed))



    """We make either the user input any image of her choice or use the default image"""
    filename = get_file()
    image = SimpleImage(filename)
    print("*******************************************HERE IS THE IMAGE YOU CHOSE OR THE DEFAULT IMAGE********************************************************")
    image.show()


    time.sleep(5)




    """This prints the total number of pixels in the image"""


    print("***************************************************************************************************************************")
    print("************************************************THE SERIES STARTS HERE********************************************************")


    """Adding the seed to the series as the first term"""
    random_number_series =[]

    random_number_series = imagerandom.ImageToRandom(filename, seed)

    print(random_number_series)




    """Printing the random series by calling ImageToRandom function in module imagerandom"""

    """Passing the inputted image and seed to our function Image To Random in module imagerandom """





    print("***************************************************************************************************************************")
    print("************************************************THE SERIES ENDS HERE********************************************************")

    time.sleep(5)

    """Storing the series in a new list random_series that will be used for plotting graph"""
    random_series = []
    random_series = random_number_series


    """Creating a list for storing the pixel numbers"""
    pixel = []
    for i in range(len(random_series)):
        pixel.append(i)

    time.sleep(5)

    """This function creates a graph of pixel number against the corresponding random number from the random series"""
    
    imagerandom.draw_graph(pixel, random_series)




def get_file():
    # Read image file path from user, or use the default file

    filename = input('Please choose the image you want with the correct path name or press enter:-')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()