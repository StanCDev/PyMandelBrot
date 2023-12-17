import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm

windows = {
    "Corn" : (-0.76007566630506, 0.08048608971789, -0.76006598207706, 0.08049577394589),
    "Reef" : (-0.10715680236336,- 0.91210879302021,-0.10715079727776, - 0.91210278793461),
    "Kaleidoscope" : (-1.74791080277175 , 0.00194115673936, -1.74790595528095 , 0.00194600423016),
    "Cornet" : (-0.76303941125246 , 0.0825324955705,-0.76272491751166 , 0.0828469893113),
    "Base" : (-2,-1,1,1)
}

def grid(w, h):
    x = np.linspace(-2,1,w)
    y = np.linspace(-1,1,h)
    xs,ys = np.meshgrid(x,y)
    Z = xs + 1j*ys
    return Z



def mandelbrot(c, n = 100):
    z = 0
    for i in range(1,n+1):
        z = z ** 2 + c
        if np.abs(z) > 2:
            return i
    return n


def grid_parallel(N, maxN=1000, x1=-2 , y1=-1, x2=1, y2=1):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    x = np.linspace(x1,x2,N)
    y = np.linspace(y1,y2,int(dy*N/dx))
    X,Y = np.meshgrid(x,y)
    C = X + 1j*Y
    
    out = np.zeros_like(C,dtype=type(mandelbrot(0)))
    Z = np.zeros_like(C,dtype=complex)
    cond = abs(Z) <= 2
    
    ##mandelbrot function
    for i in range(1,maxN+1):
        Z[cond] = Z[cond] ** 2 + C[cond]
        out[cond] += 1
        cond[cond] = (abs(Z[cond]) <= 2)
    #print(out)
    #plt.figure(figsize= (6,6))
    #plt.imshow(np.log(out+1), extent=[-2,2,-2,2])
    #plt.xlabel(r"$\Re$")
    #plt.ylabel(r"$\Im$")
    #plt.show()
    #return out
    return np.log(out+1)


N = 1_000
Nlog =np.log(N+1)
D = 10_000
(x1,y1,x2,y2) = windows["Reef"]
out = grid_parallel(D,N, x1,y1,x2,y2)
outNorm = out * 1/Nlog
im = Image.fromarray(np.uint8(cm.hot(outNorm)*255))



im.show()


im.save(f"Mandelbrot_Size:{N},Reef.PNG")