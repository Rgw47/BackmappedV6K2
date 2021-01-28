OriginalCoordinates = open("V2KCG.txt","r")

OriginalCoordinates = OriginalCoordinates.readlines()

import numpy as np

V6K2 = np.zeros((65,3),dtype = float)
CGV6K2 = np.zeros((9,3),dtype = object)

for x in range(2,11):
    for y in range(0,3):
        Bead = OriginalCoordinates[x].split('   ')
        CGV6K2[x-2,y] = Bead[y+4]
        CGV6K2[x-2,y] = float(CGV6K2[x-2,y])
    
r = ((CGV6K2[8,0]-CGV6K2[0,0])**2 + (CGV6K2[8,1] - CGV6K2[0,1])**2)**.5/9

#ACE
for x in range(0,6):
    V6K2[x,2] = CGV6K2[0,2]

#VAL1
for x in range(6,10):
    V6K2[x,2] = CGV6K2[1,2]
    V6K2[21,2] = CGV6K2[1,2]
    V6K2[22,2] = CGV6K2[1,2]

#Val2
for x in range(10,21):
    V6K2[x,2] = CGV6K2[2,2]

#VAL1
for x in range(23,27):
    V6K2[x,2] = CGV6K2[3,2]
    V6K2[38,2] = CGV6K2[3,2]
    V6K2[39,2] = CGV6K2[3,2]

#Val2
for x in range(27,38):
    V6K2[x,2] = CGV6K2[4,2]

#Lys1
for x in range(40,47):
    V6K2[x,2] = CGV6K2[5,2]
    V6K2[60,2] = CGV6K2[5,2]
    V6K2[61,2] = CGV6K2[5,2]

#Lys2
for x in range(47,56):
    V6K2[x,2] = CGV6K2[6,2]

#Lys3
for x in range(56,60):
    V6K2[x,2] = CGV6K2[7,2]

#NHE
for x in range(62,65):
    V6K2[x,2] = CGV6K2[8,2]
    
#ACE
V6K2[0,0] = CGV6K2[0,0] - r*np.cos(1.047)
V6K2[1,0] = V6K2[0,0] - r*np.cos(1.047)
V6K2[2,0] = V6K2[0,0] - r
V6K2[3,0] = V6K2[0,0] - r*np.cos(1.047)
V6K2[4,0] = CGV6K2[0,0]
V6K2[5,0] = CGV6K2[0,0] - r*np.cos(1.047)

V6K2[0,1] = CGV6K2[0,1] - r*np.sin(1.047)
V6K2[1,1] = V6K2[0,1] - r*np.sin(1.047)
V6K2[2,1] = V6K2[0,1]
V6K2[3,1] = V6K2[0,1] + r*np.sin(1.047)
V6K2[4,1] = CGV6K2[0,1]
V6K2[5,1] = CGV6K2[0,1] + r*np.sin(1.047)

V1 = np.zeros((1,3),dtype = float)
for x in range(0,6):
    V1[0,0] = V6K2[x,0] + V1[0,0]
    V1[0,1] = V6K2[x,1] + V1[0,1]
    V1[0,2] = V6K2[x,2] + V1[0,2]
V1[0,0] = V1[0,0]/5
V1[0,1] = V1[0,1]/5
V1[0,2] = V1[0,2]/5

r1 = r/2
#1Val
V6K2[8,0] = CGV6K2[1,0] - r1
V6K2[9,0] = V6K2[8,0]
V6K2[6,0] = V6K2[8,0] - r*np.cos(1.047) 
V6K2[7,0] = V6K2[6,0] - r*np.cos(1.047)
V6K2[21,0] = CGV6K2[1,0] + r1
V6K2[22,0] = V6K2[21,0] + r*np.cos(1.047)

V6K2[8,1] = CGV6K2[1,1]
V6K2[9,1] = V6K2[8,0] - r
V6K2[6,1] = V6K2[8,0] + r*np.sin(1.047) 
V6K2[7,1] = V6K2[6,0] + r*np.sin(1.047)
V6K2[21,1] = CGV6K2[1,0]
V6K2[22,1] = V6K2[21,0] - r*np.sin(1.047)

V2 = np.zeros((1,3),dtype = float)
for x in range(6,9):
    V2[0,0] = V6K2[x,0] + V2[0,0]
    V2[0,1] = V6K2[x,1] + V2[0,1]
    V2[0,2] = V6K2[x,2] + V2[0,2]
V2[0,0] = (V2[0,0]+V6K2[21,0]+V6K2[22,0])/6
V2[0,1] = (V2[0,1]+V6K2[21,1]+V6K2[22,1])/6
V2[0,2] = (V2[0,2]+V6K2[21,2]+V6K2[22,2])/6

#2Val
V6K2[10,0] = CGV6K2[2,0]
V6K2[11,0] = V6K2[10,0] + r*np.cos(1.047)
V6K2[12,0] = V6K2[10,0] - r*np.cos(1.047)
V6K2[13,0] = V6K2[12,0]
V6K2[14,0] = V6K2[12,0] - r
V6K2[15,0] = V6K2[12,0]
V6K2[16,0] = V6K2[12,0]
V6K2[17,0] = V6K2[10,0] + r*np.cos(1.047)
V6K2[18,0] = V6K2[17,0] + r
V6K2[19,0] = V6K2[17,0]
V6K2[20,0] = V6K2[17,0] - r

V6K2[11,1] = CGV6K2[2,1]
V6K2[12,1] = V6K2[10,1] + r*np.sin(1.047)
V6K2[13,1] = V6K2[10,1] - r*np.sin(1.047)
V6K2[14,1] = V6K2[12,1] + r
V6K2[15,1] = V6K2[12,1]
V6K2[16,1] = V6K2[12,1] - r
V6K2[17,1] = V6K2[10,1] - r*np.sin(1.047)
V6K2[18,1] = V6K2[17,1]
V6K2[19,1] = V6K2[17,1] - r
V6K2[20,1] = V6K2[17,1]

V3 = np.zeros((1,3),dtype = float)
for x in range(10,21):
    V3[0,0] = V6K2[x,0] + V3[0,0]
    V3[0,1] = V6K2[x,1] + V3[0,1]
    V3[0,2] = V6K2[x,2] + V3[0,2]
V3[0,0] = V3[0,0]/10
V3[0,1] = V3[0,1]/10
V3[0,2] = V3[0,2]/10

#1Val
V6K2[25,0] = CGV6K2[3,0] - r1
V6K2[26,0] = V6K2[24,0]
V6K2[23,0] = V6K2[24,0] - r*np.cos(1.047) 
V6K2[24,0] = V6K2[22,0] - r*np.cos(1.047)
V6K2[38,0] = CGV6K2[3,0] + r1
V6K2[39,0] = V6K2[38,0] + r*np.cos(1.047)

V6K2[25,1] = CGV6K2[3,1]
V6K2[26,1] = V6K2[24,1] - r
V6K2[23,1] = V6K2[24,1] + r*np.sin(1.047) 
V6K2[24,1] = V6K2[22,1] + r*np.sin(1.047)
V6K2[38,1] = CGV6K2[3,1]
V6K2[39,1] = V6K2[38,1] - r*np.sin(1.047)

V4 = np.zeros((1,3),dtype = float)
for x in range(23,27):
    V4[0,0] = V6K2[x,0] + V4[0,0]
    V4[0,1] = V6K2[x,1] + V4[0,1]
    V4[0,2] = V6K2[x,2] + V4[0,2]
V4[0,0] = (V4[0,0]+V6K2[38,0]+V6K2[39,0])/6
V4[0,1] = (V4[0,1]+V6K2[38,1]+V6K2[39,1])/6
V4[0,2] = (V4[0,2]+V6K2[38,2]+V6K2[39,2])/6

#2Val
V6K2[27,0] = CGV6K2[4,0]
V6K2[28,0] = V6K2[26,0] + r*np.cos(1.047)
V6K2[29,0] = V6K2[26,0] - r*np.cos(1.047)
V6K2[30,0] = V6K2[28,0]
V6K2[31,0] = V6K2[28,0] - r
V6K2[32,0] = V6K2[28,0]
V6K2[33,0] = V6K2[26,0]
V6K2[34,0] = V6K2[26,0] + r*np.cos(1.047)
V6K2[35,0] = V6K2[34,0] + r
V6K2[36,0] = V6K2[34,0]
V6K2[37,0] = V6K2[34,0] - r

V6K2[27,1] = CGV6K2[4,1]
V6K2[28,1] = V6K2[26,1] + r*np.sin(1.047)
V6K2[29,1] = V6K2[26,1] - r*np.sin(1.047)
V6K2[30,1] = V6K2[28,1] + r
V6K2[31,1] = V6K2[28,1]
V6K2[32,1] = V6K2[28,1] - r
V6K2[33,1] = V6K2[26,1]
V6K2[34,1] = V6K2[26,1] - r*np.sin(1.047)
V6K2[35,1] = V6K2[34,1]
V6K2[36,1] = V6K2[34,1] + r
V6K2[37,1] = V6K2[34,1]

V5 = np.zeros((1,3),dtype = float)
for x in range(27,38):
    V5[0,0] = V6K2[x,0] + V5[0,0]
    V5[0,1] = V6K2[x,1] + V5[0,1]
    V5[0,2] = V6K2[x,2] + V5[0,2]
V5[0,0] = V5[0,0]/10
V5[0,1] = V5[0,1]/10
V5[0,2] = V5[0,2]/10

#LYs1
V6K2[42,0] = CGV6K2[5,0]
V6K2[43,0] = V6K2[42,0] - r1*np.cos(0.523599)
V6K2[40,0] = V6K2[42,0] - r 
V6K2[41,0] = V6K2[40,0] - r1
V6K2[44,0] = V6K2[42,0]
V6K2[45,0] = V6K2[44,0] + r1*np.cos(1.047)
V6K2[46,0] = V6K2[44,0] - r1*np.cos(1.047)
V6K2[60,0] = V6K2[42,0] + r
V6K2[61,0] = V6K2[59,0] + r1

V6K2[42,1] = CGV6K2[5,1]
V6K2[43,1] = V6K2[42,1] - r1*np.cos(0.523599)
V6K2[40,1] = V6K2[42,1]
V6K2[41,1] = V6K2[40,1]
V6K2[44,1] = V6K2[42,1] + r
V6K2[45,1] = V6K2[44,1] + r1*np.cos(1.047)
V6K2[46,1] = V6K2[44,1] - r1*np.cos(1.047)
V6K2[60,1] = V6K2[42,0] + r
V6K2[61,1] = V6K2[59,0] + r1

V6 = np.zeros((1,3),dtype = float)
for x in range(40,47):
    V6[0,0] = V6K2[x,0] + V6[0,0]
    V6[0,1] = V6K2[x,1] + V6[0,1]
    V6[0,2] = V6K2[x,2] + V6[0,2]
V6[0,0] = (V6[0,0]+V6K2[60,0]+V6K2[61,0])/9
V6[0,1] = (V6[0,1]+V6K2[60,1]+V6K2[61,1])/9
V6[0,2] = (V6[0,2]+V6K2[60,2]+V6K2[61,2])/9

#Lys2
V6K2[47,0] = CGV6K2[6,0]
V6K2[48,0] = V6K2[47,0]
V6K2[49,0] = V6K2[47,0]
V6K2[50,0] = V6K2[47,0] - r
V6K2[51,0] = V6K2[50,0]
V6K2[52,0] = V6K2[50,0]
V6K2[53,0] = V6K2[47,0] + r
V6K2[54,0] = V6K2[53,0]
V6K2[55,0] = V6K2[53,0]

V6K2[47,1] = CGV6K2[6,1]
V6K2[48,1] = V6K2[47,1] + r
V6K2[49,1] = V6K2[47,1] + r
V6K2[50,1] = V6K2[47,1]
V6K2[51,1] = V6K2[50,1] + r
V6K2[52,1] = V6K2[50,1] + r
V6K2[53,1] = V6K2[47,1]
V6K2[54,1] = V6K2[53,1] + r
V6K2[55,1] = V6K2[53,1] + r

V7 = np.zeros((1,3),dtype = float)
for x in range(47,56):
    V7[0,0] = V6K2[x,0] + V7[0,0]
    V7[0,1] = V6K2[x,1] + V7[0,1]
    V7[0,2] = V6K2[x,2] + V7[0,2]
V7[0,0] = (V7[0,0])/8
V7[0,1] = (V7[0,1])/8
V7[0,2] = (V7[0,2])/8

#Lys3
V6K2[56,0] = CGV6K2[7,0]
V6K2[57,0] = V6K2[56,0] + r*np.cos(1.047)
V6K2[58,0] = V6K2[56,0] - r*np.cos(1.047)
V6K2[59,0] = V6K2[56,0]

V6K2[56,1] = CGV6K2[7,1]
V6K2[57,1] = V6K2[56,1] - r*np.sin(1.047)
V6K2[58,1] = V6K2[56,1] - r*np.sin(1.047)
V6K2[59,1] = V6K2[56,1] + r

V8 = np.zeros((1,3),dtype = float)
for x in range(56,60):
    V8[0,0] = V6K2[x,0] + V8[0,0]
    V8[0,1] = V6K2[x,1] + V8[0,1]
    V8[0,2] = V6K2[x,2] + V8[0,2]
V8[0,0] = (V8[0,0])/4
V8[0,1] = (V8[0,1])/4
V8[0,2] = (V8[0,2])/4

#NHE
V6K2[62,0] = CGV6K2[8,0]
V6K2[63,0] = V6K2[62,0] + r*np.cos(1.047)
V6K2[64,0] = V6K2[62,0] - r*np.cos(1.047)

V6K2[62,1] = CGV6K2[8,1]
V6K2[63,1] = V6K2[62,1] + r*np.sin(1.047)
V6K2[64,1] = V6K2[62,1] + r*np.sin(1.047)
                            
V9 = np.zeros((1,3),dtype = float)
for x in range(62,65):
    V9[0,0] = V6K2[x,0] + V9[0,0]
    V9[0,1] = V6K2[x,1] + V9[0,1]
    V9[0,2] = V6K2[x,2] + V9[0,2]
V9[0,0] = (V9[0,0])/3
V9[0,1] = (V9[0,1])/3
V9[0,2] = (V9[0,2])/3

X = np.zeros((65,1), dtype = float)
Y = np.zeros((65,1), dtype = float)
Z = np.zeros((65,1), dtype = float)

for x in range(0,65):
    X[x] = V6K2[x,0]
    Y[x] = V6K2[x,1]
    Z[x]  = V6K2[x,2]

print(V1)
print(V2)
print(V3)
print(V4)
print(V5)
print(V6)
print(V7)
print(V8)
print(V9)
#Plots your data for visualization. The Colors are
    #Black for the course-grained, colors for backmapped
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')

ax.scatter(X,Y,Z, c='r', marker='o')

plt.show()


#V6 = str(V6)

#OriginalCoordinates1 = open("V.txt","w")

#OriginalCoordinates1 = OriginalCoordinates1.writelines(V6)
