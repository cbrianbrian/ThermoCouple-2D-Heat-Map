#Created by Brian C

import numpy as np
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

#####################################################################################################
def getcsv(csvfile):
    data = pd.read_csv(csvfile)
    return data

#assuming csvfile is in this directory, otherwise change
directory = #directory where ConeTemp csv files are located is pasted here. Don't forget to include second slash '\'
#file name in directory
#filename = 'ConeTemp20psi350c040124.csv'

print ('A = ConeTemp20psi200c032824') 
print ('B = ConeTemp30psi200c032824')
print ('C = ConeTemp20psi350c040124')
print ('D = ConeTemp20psi350c040224')
print ('E = ConeTemp20psi350c2mm040224')
print ('F = ConeTemp40psi350c040324')
print ('G = ConeTemp40psi350c2mm040324')
print('H = ConeTemp40psi350c5mm040524')
print('I = ConeTemp40psi350c10mm040524')
print('J = ConeTemp20psi350c040524')
print('K = ConeTemp20psi350c2mm040524')
print('L = ConeTemp20psi350c5mm041624.csv')
filename = input ("which data set would you like to plot? A , B , C, D, E, F, G, H, I, J, K, L? ")

if filename == 'A':
    filename = 'ConeTemp20psi200c032824.csv'
    title = '20psi, 200c, surface, 03/28/24'
    center = [7, 12]
if filename == 'B':
    filename = 'ConeTemp30psi200c032824.csv'
    title = '30psi, 200c, surface, 03/28/24'
    center = [7, 12]
if filename == 'C':
    filename = 'ConeTemp20psi350c040124.csv'
    title = '20psi, 350c, surface, omega, 04/01/24'
    center = [6,13.5]
if filename == 'D':
    filename = 'ConeTemp20psi350c040224.csv'
    title = '20psi, 350c, surface, 04/02/24'
    center = [6.5,13]
if filename == 'E':
    filename = 'ConeTemp20psi350c2mm040224.csv'
    title = '20psi, 350c, 2mm, 04/02/24'
    center = [6, 13]
if filename == 'F':
    filename = 'ConeTemp40psi350c040324.csv'
    center = [8, 11.5]
    title = "40psi, 350c, surface, 04/03/24"
if filename == 'G':
    filename = 'ConeTemp40psi350c2mm040324.csv'
    center = [8, 11.5]
    title = "40psi, 350c, 2mm, 04/03/24"
if filename == 'H':
    filename = 'ConeTemp40psi350c5mm040524.csv'
    title = "40psi, 350c, 5mm, 04/05/24"
    center = [8,12]
if filename == 'I':
    filename = 'ConeTemp40psi350c10mm040524.csv'
    title = "40 psi, 350c, 10mm, 04/05/24"
    center = [7.5,11]
if filename == 'J':
    filename = 'ConeTemp20psi350c040524.csv'
    title = "20 psi, 350c, surface, 04/05/24"
    center = [7,11]
if filename == 'K':
    filename = 'ConeTemp20psi350c2mm040524.csv'
    title = "20 psi, 350c, 2mm, 04/05/24"
    center = [7.5,11]
if filename == 'L':
    filename = 'ConeTemp20psi350c5mm041624.csv'
    title = "20 psi, 350c, 5mm, 04/16/24"
    center = [7,12]

#dataset
filename = directory + filename #need to include 'directory' since csv in same folder as code
x = getcsv(filename)['x'] - center[0]
y = getcsv(filename)['y'] - center[1]
T = getcsv(filename)['T']
###################################################################################

df=pd.DataFrame(data={'A':x,'B':y,'C':T})

fig = plt.figure()

#####   SCATTER PLOT AND COLORBAR    ########
points = plt.scatter(df.A, df.B, c=df.C,cmap="jet", lw=10)
m = cm.ScalarMappable(cmap=cm.jet)                              # WHAT DO THESE
m.set_array(df['C'])                                            # TWO LINES DO?
plt.colorbar(points)
plt.title(title)

###### TEMPERATURE VALUES AT EACH POINT #########
for i in range(len(df)):
    plt.text(df.loc[i, "A"]-.2,df.loc[i, "B"]-.3, df['C'].astype(str)[i]) 

####### 3 HOTTEST AND 3 COLDEST VALUES ##########
largest = df.nlargest(3, ['C'])
for i in range(len(largest)):
    plt.text(largest.iat[i, 0]-.2, largest.iat[i, 1]-.6, 'HOT', color = 'red') 

smallest = df.nsmallest(3, ['C'])
for i in range(len(smallest)):
    plt.text(smallest.iat[i, 0]-.2, smallest.iat[i, 1]-.6, 'COLD', color = 'blue') 
    
######    CONE HOLE     ############
theta = np.linspace(-np.pi, np.pi, 200)
plt.plot(3*np.sin(theta), 3*np.cos(theta), color= 'black')

plt.show()

