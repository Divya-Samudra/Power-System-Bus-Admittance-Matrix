##---Neglecting shunt admittances and mutual coupling
import numpy as np

#input data:
#1-element no. 2-from bus, 3-to bus, 4-primitive impedance

line_data = np.array([[1,1,2,0+0.5j],[2,1,3,0+0.45j],[3,4,2,0+0.4j],[4,3,2,0+0.3j],[5,3,4,0+0.35j]])
print("line data = ",line_data)

# no. of elements and buses

elements = len(line_data)
print("no. of elements = ",elements)

bus1 = max(line_data[:,1]).real
bus2 = max(line_data[:,2]).real
bus =int(max(bus1,bus2))
print("no. of buses = ",bus)

#Zprimitive of order exe

zprimitive = np.zeros((elements,elements),dtype=np.complex_)
for i in range(0,elements,1):
    zprimitive[i][i] = line_data[i][3]
print("Zprimitive = ",zprimitive)

#Yprimitive

yprimitive = np.linalg.inv(zprimitive)
print("Yprimitive = ",yprimitive)
 
#bus incidence matrix

A = np.zeros((elements,bus),dtype=np.int)
for i in range(0,elements,1):
    pos1 = int(line_data[i][1].real)
    pos2 = int(line_data[i][2].real)
    A[i][pos1-1] = 1
    A[i][pos2-1] = -1
print("Bus incidence matrix = ",A)
  
#YBUS of order nxn

Ybus1 = np.dot(A.transpose(),yprimitive)
Ybus = np.dot(Ybus1,A)
print("Ybus = ",Ybus)

