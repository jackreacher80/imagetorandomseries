"""This module is created to access the function that generates random series."""
from simpleimage import SimpleImage
import matplotlib.pyplot as plt
import time
import random


"""The formula used to create a random number series as per LCG algorithm is Xn+1= (aXn + c)mod m. I have used the values of pixel.red,
pixel.green and pixel.blue as a,c,m to add to the randomness of the equation. The seed Xn is generated by the product of a random timestamp
value and the random value given by randint function"""
def ImageToRandom(filename, xn):
    image = SimpleImage(filename)
    seed = xn


    """This list is created to store the random numbers in the series"""
    new_random_series = [seed]
    print(new_random_series)
    #new_random_series= new_random_series.append(xn)
    #print(new_random_series)
    for pixel in image:
        a = pixel.red
        c = pixel.green
        m = pixel.blue


        """m cannot be zero for modulo to function so we use continue to move to the next number in the loop"""
        if m == 0:
            continue
        """m needs to be prime so we use this condition to see if m is prime or not"""
        if(is_prime(m)):
            continue
        #print("m is prime and its value is= " + str(m))


        """This LCG formula creates the next term but I have multiplied it by randint function again to add more randomness"""
        xnplusone = (float(((a * xn) + c) % m))

        new_random_series.append(xnplusone)


        xn = xnplusone

    #new_random_series.insert(0, seed)
    print(new_random_series[0], new_random_series[1], new_random_series[2])
    print("length of the series is" + str(len(new_random_series)))

    return new_random_series


"""This function checks if m is prime or not and returns a boolean value back"""
def is_prime(m):
    if m == 1:
        return True
    for i in range(2,int(m)):
        if m % i == 0:
            return True
    return False




def draw_graph(pixel, random_series):
    x = pixel
    y = random_series

    #time.sleep(5)


    #print("***************************************THESE ARE THE CO-ORDINATES*************************************************************")

    #for i in range(len(random_series)):
        #print("co-ordinates are-"+ "(" + str(x[i]) + "," + str(y[i]) + ")")

    time.sleep(5)

    #print("***************************************HERE IS THE GRAPH BETWEEN PIXELS AND CORRESPONDING RANDOM NUMBER****************************************************************************************************************")
    plt.xlabel('pixel')
    plt.ylabel('random number')
    plt.title('pixel-random number graph!')

    plt.plot(x, y)

    plt.show()








        


    