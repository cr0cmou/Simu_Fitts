from scipy.optimize import minimize_scalar
import numpy
import scipy
import matplotlib.pyplot as plt
import scipy.special

D = 8192
W = 10
penalite = 1.5 #temps en secondes compris entre 0.6 et 2.1

#ID 3.6 : D = 512, W = 46
#ID 7 : D = 1024, W = 8
#ID 9.6 : D = 8192, W = 10

fig, ax = plt.subplots()


valeursDeB = numpy.linspace(0.1, 0.33, 5)

for b in valeursDeB :

    valeursDeA = numpy.linspace(-0.4, 0.1, 5)
    optiError = []
    
    for a in valeursDeA :
         
        def simulation(e) :
            return a + b * numpy.log2(1 + (D * numpy.sqrt(2) * scipy.special.erfinv(1-e)) / (2.066 * W))+ e*penalite
        
        result = minimize_scalar(simulation, bounds = (0, 1))
        optiError.append(result.x)
        
    ax.plot(valeursDeA, optiError, label="b : "+str(b))

ax.set_xlabel("valeur de a")
ax.set_ylabel("taux d'erreur optimal")
ax.legend()

plt.ion()
plt.show(block=True)