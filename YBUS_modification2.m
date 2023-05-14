% Program to calculate Ybus using Singular transformation
clc; clear;

%input line data
%1-element no. 2-from bus, 3-to bus, 4-primitive impedance, 5-element
%coupled to, 6-coupling impedance
line_data =[1 1 0 -j*5 0 0;
            2 3 0 -j*5 0 0;
            3 2 0 -j*5 0 0;
            4 1 2 j*0.5 0 0;
            5 2 3 j*0.4 6 j*0.2;
            6 1 3 j*0.25 5 j*0.2];
 
 % No. of elements and buses
 elements = max(line_data(:,1));
 buses = max(max(line_data(:,2)),max(line_data(:,3)));
 
 % Zprimitive of order exe 
 zprimitive = zeros(elements,elements); %sparse
 for i = 1:elements
     zprimitive(i,i) = line_data(i,4); % self impedances
     if(line_data(i,5)~=0) %-------mutual impedance
         j = line_data(i,5);
         zmutual = line_data(i,6);
         zprimitive(i,j) = zmutual;
     end
 end
 
 %Yprimitive
 yprimitive = inv(zprimitive)
  
 %bus incidence matrix of order exn
 A = zeros(elements,buses); % sparse
 for i = 1: elements
     if line_data(i,2)~=0 % not bus0
         A(i,line_data(i,2)) = 1;
     end
     if line_data(i,3)~=0 %not bus0
         A(i,line_data(i,3)) = -1;
     end
 end
 A
 
 % YBUS of order nxn
 Ybus = A.'*yprimitive*A
 