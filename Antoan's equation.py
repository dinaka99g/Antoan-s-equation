import numpy as np
import math
import matplotlib
font = {'family' : 'sans-serif',
        'weight' : 'medium',
        #'style'  : 'italic',
        'size'   : 10}

matplotlib.rc('font', **font)
from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import filedialog, Text
import os

def flnp(a, b, c, t):
    return math.exp( a - (b/(t+c)))

def plot(master, A, B, C, T1, T2, Name):

    name = Name.get()
    a = float(A.get())
    b = float(B.get())
    c = float(C.get())
    t1 = float(T1.get())
    t2 = float(T2.get())

    deltat = abs(t1-t2)
    n = deltat/1000

    t = np.arange(t1, t2, n)
    lnp = []
    for temp in t:
        lnp.append(flnp(a, b, c, temp))

    plt.plot(t, lnp, 'k-', label = name, linewidth=1)
    plt.legend()

    plt.xlabel("t [$\degree$C]")
    plt.ylabel("p$^{*}$ [kPa]")

    plt.xlim(t1, t2)


    plt.tick_params(width=2, length=6, which='both')
    plt.show()


def main():


    master = tk.Tk()
    master.title("Antoine equation")

    up = tk.IntVar()



    
    label1 = tk.Label(master, text="A").grid(row=1)
    label2 = tk.Label(master, text="B").grid(row=2)
    label3 = tk.Label(master, text="C").grid(row=3)
    label4 = tk.Label(master, text="Lower bound temp.").grid(row=4)
    label5 = tk.Label(master, text="Upper bound temp.").grid(row=5)
    label6 = tk.Label(master, text="Fluid name").grid(row=6)
    A = tk.Entry(master)
    B = tk.Entry(master)
    C = tk.Entry(master)
    T1 = tk.Entry(master)
    T2 = tk.Entry(master)
    Name = tk.Entry(master)

    A.grid(row=1, column=1)
    B.grid(row=2, column=1)
    C.grid(row=3, column=1)
    T1.grid(row=4, column=1)
    T2.grid(row=5, column=1)
    Name.grid(row=6, column=1)

    button1 = tk.Button(master, text='Plot', command=lambda : plot(master, A, B, C, T1, T2, Name))
    button1.grid(row=7, column= 1)
    master.mainloop()

if __name__=="__main__":
    main()