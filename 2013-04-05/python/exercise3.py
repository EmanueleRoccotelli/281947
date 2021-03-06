#Fella Davide - 281947
from pyplasm import *;

#Varibiali
altezzaMuro = 4
solaio = 0.74
spessoremuri = 0.4

altezzaFinestraStretta = 3
larghezzaFinestraStretta = 0.7
spazioFinestraStrettaMuro = 0.5


GRID = COMP([INSR(PROD),AA(QUOTE)])


facciataNordFloor1= GRID([ [9.70], [0.4], [-4.74,4]])
facciataNordFloor2= GRID([ [9.70], [0.4], [-8.74,4]])
facciataNordFloor3= GRID([ [9.70], [0.4], [-12.74,4]])


finestraRettangoloF1 = STRUCT([ T([1,3])([0.5, 6.24]), (CUBOID([6,0.4,2]))])
finestraLungaF1 = STRUCT([ T([1,3])([8,(altezzaMuro+solaio+spazioFinestraStrettaMuro)]), (CUBOID([0.7,0.4,3]))])

facciataNordFloor1 = STRUCT([DIFFERENCE([facciataNordFloor1, finestraRettangoloF1, finestraLungaF1   ])])
facciataNordFloor2 = STRUCT([T(3)((altezzaMuro+solaio)),(facciataNordFloor1)])
facciataNordFloor3 = STRUCT([T(3)((altezzaMuro+solaio)*2),(facciataNordFloor1)])

facciataNordFloor0 = CUBOID([3.78,0.4,4])
facciataNordFloor0 = STRUCT([T(1,2)(5.85,2.51),(facciataNordFloor0)])

northFace = STRUCT([facciataNordFloor1,facciataNordFloor2,facciataNordFloor3,facciataNordFloor0 ])



murobassoSud = STRUCT([T([1,2])([2.93, 2.11]), (CUBOID([4.51,0.4,4]))])
finestraMuroBassoSud = STRUCT([T([1,2,3])([3.1, 2.11,2.1]), (CUBOID([2,0.4,1.5]))])
murobassoSud =  STRUCT([DIFFERENCE([murobassoSud, finestraMuroBassoSud])])

facciataFloor0Sud = STRUCT([murobassoSud])


facciataSudfloor1 = GRID([ [9.70], [0.4], [-4.74,4]])

finestralungaFloor1 = STRUCT([T([1,3])([0.70, 4.75]), (CUBOID([1,0.4,3]))])
finestraQuadrataFloor1Sud = GRID([ [-2.70, 1.6, -0.2, 1.6, -0.2, 1.6, -0.2, 1.6], [0.4], [-0.25,1.65,-0.2, 1.65]])


facciataSudfloor1 = STRUCT([DIFFERENCE([facciataSudfloor1, finestralungaFloor1, finestraQuadrataFloor1Sud])])



