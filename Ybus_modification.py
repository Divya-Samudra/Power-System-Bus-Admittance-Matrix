#Program to calculate Ybus using Singular Transformation
import numpy as np

#input data: line data- ex6 matrix
#1-element no. 2-from bus, 3-to bus, 4-primitive impedance
#5-elementcoupled to, 6-coupling impedance
line_data1 = [[1,1,0,0-5j,0,0],[2,3,0,0-5j,0,0],[3,2,0,0-5j,0,0],[4,1,2,0+0.5j,0,0],[5,2,3,0+0.4j,6,0+0.2j],[6,1,3,0+0.25j,5,0+0.2j]]
print("line data = ",line_data1)
line_data = np.array(line_data1)

# no. of elements
elements = len(line_data)
print("no. of elements = ",elements)
#no.of buses
bus1 = max(line_data[:,1]).real
bus2 = max(line_data[:,2]).real
bus =int(max(bus1,bus2))
print("no. of buses = ",bus)

#Zprimitive of order exe
zprimitive = np.zeros((elements,elements),dtype=np.complex_) #sparse
for i in range(0,elements,1):
    zprimitive[i][i] = line_data[i][3]  #self impedance
    if (line_data[i][4]!=0):
        j =int((line_data[i][4]-1).real)
        zmutual =line_data[i][5]    #mutual impedance
        zprimitive[i][j] =zmutual 
print("Zprimitive = ",zprimitive)

#Yprimitive
yprimitive = np.linalg.inv(zprimitive)
print("Yprimitive = ",yprimitive)
 
#bus incidence matrix of order exn
A = np.zeros((elements,bus),dtype=np.int)   #sparse
for i in range(0,elements,1):
    pos1 = int((line_data[i][1]).real)
    pos2 = int((line_data[i][2]).real)
    if (pos1!=0):   #not bus0
        A[i][pos1-1] = 1
    if (pos2!=0):   #not bus0
        A[i][pos2-1] = -1
print("Bus incidence matrix = ",A)
  
#YBUS of order nxn
Ybus1 = np.dot(A.transpose(),yprimitive)
Ybus = np.dot(Ybus1,A)
print("Ybus = ",Ybus)

