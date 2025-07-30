from scipy.optimize import minimize_scalar
import numpy
import scipy
import matplotlib.pyplot as plt
import scipy.special

a = -0.4
b = 0.1

#ID 3.6 : D = 512, W = 46
#ID 7 : D = 1024, W = 8
#ID 9.6 : D = 8192, W = 10

fig, ax = plt.subplots()


penalites = numpy.linspace(0.6, 2.1, 6)

for p in penalites :

    valeursID = [ (512, 46), (1024, 8), (8192, 10) ] #3 tuples (D, W) donnant des ID valant 3.6, 7, et 9.6
    final = [ numpy.log2(1 + id[0]/id[1]) for id in valeursID ]
    optiError = []
    
    for id in valeursID :
         
        def simulation(e) :
            return a + b * numpy.log2(1 + (id[0] * numpy.sqrt(2) * scipy.special.erfinv(1-e)) / (2.066 * id[1]))+ e*p
        
        result = minimize_scalar(simulation, bounds = (0, 1))
        optiError.append(result.x)
        
    ax.plot(final, optiError, label="penalité : "+str(p))

ax.set_xlabel("valeur de ID")
ax.set_ylabel("taux d'erreur optimal")
ax.legend()

plt.ion()
plt.show(block=True)