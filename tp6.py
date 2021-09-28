import random
import numpy as np
from math import e, modf

ln = np.log


N = 2
TF = 9600
#TA = 10*random.random()+20
#IA = ln(-random.random()+1)/-0.0001

t = 0
tpll = 0
tpv = 9600
pac_rec = 0 ##PCR, Pacientes Con Receta
nt = 0
ns = 0
sto = 0
ito = 0
atendidos = 0
tat = 0
nat = 0
cant_arr = 0 ## arrepentidos

while t<TF:
    if tpll<=tpv:
        t = tpll
        random1 = random.random()
        if random1<0.7:
            pac_rec = pac_rec + 1
            nt = nt + 1
            tpll = t + 10*random.random()+35
        else:
            tpll = t + 10*random.random()+35
            r = random.random()
            if r<0.7:
                ns = ns + 1
            else:
                cant_arr = cant_arr + 1
            nt = nt + 1
    else:
        t = tpv
        if ns>0:
            sto = sto + (t -ito)
            ta = 10*random.random()+20
            tpv = tpv + ta
            atendidos = atendidos + 1
            ns = ns - 1
            tat = tat + ta
            if atendidos == 12 or t>(tpv-tat)+480:
                atendidos = 0
                nat = nat + ns
                tpv = tpv + 2500
        else:
            ito = t


def arrepentimiento(espera):
    dias_espera = espera%12

    if dias_espera == 0:
        return False
    else:
        if dias_espera < 60:
            return False
        else:
            if random() < 0.7:
               return True
            else:
                return False

            


print ('Personas en el sistema: ',ns)
print ('Cantidad de arrepentidos en el sistema: (x100) ', cant_arr)
print ('Sumatoria de tiempo ocioso: (x100)', sto/t)    
print ('Pacientes no atendidos: ', nat/ns)