#Get csv data and save into a list
import csv
import pandas as pd
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def getcsv(csvfile):
    data = pd.read_csv(csvfile)
    return data

#assuming csvfile is in this directory, otherwise change
directory = #input directory path where .csv file are located
#file name in directory
#filename = 'ConeTemp20psi350c040124.csv'

A = 'ConeTemp20psi350c040124.csv'
B = 'ConeTemp30psi200c032824.csv'
C = 'ConeTemp20psi200c032824.csv'
D = 'ConeTemp20psi350c040224.csv'
E = 'ConeTemp20psi350c2mm040524.csv'


print ('A = '+ A)
print ('B = '+ B)
print ('C = '+ C) 
print ('D = '+ D)
print ('E = '+ E)
filename = input ("which data set would you like to plot? A , B , C, D, E? ")

if filename == 'A':
    filename = 'ConeTemp20psi350c040124.csv'
if filename == 'B':
    filename = 'ConeTemp30psi200c032824.csv'
if filename == 'C':
    filename = 'ConeTemp20psi200c032824.csv'
if filename == 'D':
    filename = 'ConeTemp20psi350c040224.csv'
if filename == 'E':
    filename = 'ConeTemp20psi350c2mm040524.csv'

#dataset
filename = directory + filename # need to include 'directory' since csv not in same folder as code

x = getcsv(filename)['x'] 
y = getcsv(filename)['y'] 
T = getcsv(filename)['T']

#Creating figure
fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection ="3d")
   
#Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.3, 
        alpha = .3) 
 
#Creating color map
my_cmap = plt.get_cmap('hsv')
 
#Creating plot
sctt = ax.scatter3D(x, y, T,
                    alpha = 1,
                    c = (x + y + T), 
                    cmap = my_cmap, 
                    marker ='^')



if filename == A:
    plt.title("20psi, 350degC, Omega")
elif filename == B:
    plt.title("30psi, 200degC")
elif filename == C:
    plt.title("20psi, 200degc")
if filename == D:
    plt.title("20psi, 350degC, Fluke")
if filename == E:
    plt.title("20psi, 350degC, 2mm")
   
ax.set_xlabel('X-axis (mm)', fontweight ='bold') 
ax.set_ylabel('Y-axis (mm)', fontweight ='bold') 
ax.set_zlabel('Temperature(degC)', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
 
# show plot
plt.show()
