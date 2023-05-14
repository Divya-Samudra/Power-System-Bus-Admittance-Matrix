clc; clear;
 
% Neglecting shunt admittances and mutual coupling

%input data:
%1-element no. 2-from bus, 3-to bus, 4-primitive impedance
line_data =[1 1 2 j*0.5;
            2 1 3 j*0.45;
            3 4 2 j*0.4;
            4 3 2 j*0.3;
            5 3 4 j*0.35];

        % Zprimitive of order exe
 elements = max(line_data(:,1));
 zprimitive = zeros(elements,elements);
 for i = 1:elements
     zprimitive(i,i) = line_data(i,4); % self impedances
 end
 
 %Yprimitive
 yprimitive = inv(zprimitive)
 
  buses = max(max(line_data(:,2)),max(line_data(:,3)));
 %bus incidence matrix
 A = zeros(elements,buses);
 for i = 1: elements
     A(i,line_data(i,2)) = 1;
     A(i,line_data(i,3)) = -1;
 end
 A
 % YBUS of order nxn
 Ybus = A.'*yprimitive*A
 