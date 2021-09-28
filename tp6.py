import random,sys
import numpy as np
from math import e, modf

ln = np.log


n =0
TF = 14405 #30 dias

#TA = 10*random.random()+20
#IA = ln(-random.random()+1)/-0.0001

def arrepentimiento(personas):
    dias_espera = int(personas/12)*2400

    if dias_espera >= 0 and dias_espera <15*480: #si espera 2 semanas
        return False
    else:
        if random.random() < 0.7:
            return True
        else:
            return False

def simular():
    t = 0
    tpll = 0
    tpv = 8*60*31/n
    inicial_tiempo = tpv
    pac_rec = 0
    nt = 0
    pac_oftal = 0
    ns = 0
    sto = 0
    ito = 0
    atendidos = 0
    tat = 0
    nat = 0
    cant_arr = 0
    aux = tpv
    encolados=0
    while t<TF:
        if tpll<=tpv:
            t = tpll
            tpll = t + 10*random.random()+55
            random1 = random.random()
            if random1<0.3:
                pac_rec = pac_rec + 1
                nt = nt + 1
            else:
                if not(arrepentimiento(ns)):
                    ns = ns + 1
                    encolados=encolados+1
                    pac_oftal = pac_oftal + 1
                    ito = t
                    if ns == 1:
                        tpv = aux + t
                else:
                    cant_arr = cant_arr + 1
                nt = nt + 1
        else:
            t = tpv
            if ns>0:
                ta = 10*random.random()+20
                tpv = tpv + ta
                atendidos = atendidos + 1
                ns = ns - 1
                tat = tat + ta
                sto = sto + (t-ito)
                ito = t
                encolados=encolados-1
                if atendidos == 12 or t>(tpv-tat)+inicial_tiempo:
                    atendidos = 0
                    nat = nat + encolados
                    encolados=0
                    tpv = (tpv - tat ) + inicial_tiempo
                    if(ns==0):
                       aux = tpv
                       tpv = 9999999999 
            else:
                aux = tpv
                tpv = 9999999999

    return nt,ns,pac_oftal, (cant_arr/nt)*100 , (sto/TF)*100,nat
            
def resultados(nt,ns,pac_oftal,SARR,PTO,nat):
    print ('Personas en el sistema totales: ',nt)
    print ('Personas en el sistema sin atenderse por fin de la simulacion: ',ns)
    print ('Personas en el sistema oftalmologo: ',pac_oftal)
    ##print ('Cantidad de arrepentidos en el sistema: ', (cant_arr/nt)*100, '%')
    print ('Cantidad de arrepentidos en el sistema: ', SARR, '%')
    print ('Porcentaje de tiempo ocioso:', PTO ,'%')    
    print ('Pacientes no atendidos, que estaban esperando al oftalmologo: ', nat)
    
if __name__ == "__main__":

    # Parametros
    n= int(sys.argv[1])
    NT,NS,PAC_OFTAL,SARR,PTO,NAT=simular()
    print('con N= ',n)
    resultados( NT,NS,PAC_OFTAL,SARR,PTO,NAT)
    
    
