import generate
import io 

loop = True

while loop:
    print("Welcome to PyMandelbrot. Enter information to obtain a generated image of the mandelbrot set")

    # loaded = input("Enter y if you want to use a preloaded location, else enter n: \n")

    print("Start by entering the coordinates of the window in the form: (x1,y1,x2,y2): lower left corner and upper right corner")

    x1 = float(input("x1: \n"))
    y1 = float(input("y1: \n")) 
    x2 = float(input("x2: \n")) 
    y2 = float(input("y2: \n"))


    print("Now specify the width of your images in pixels: (the height will be scaled accordingly)")
    N = int(input("Width: \n"))

    saveIm = input("Would you like to save the image ? [y] / [n] : \n")
    save = False
    saveName = ""

    if saveIm == "y":
        save = True
        saveName = input("Finally please specify name of saved image: \n")


    print("image is being generated ...")

    generate.plot(N, x1, y1, x2, y2, save, saveName)

    regen = input("Do you want to generate another image? [y] / [n] : \n")

    if regen == "n":
        loop = False