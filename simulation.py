import matplotlib.pyplot as plt
import numpy
import scipy
import scipy.special
a = 0.1 #temps constant présent dans toute tâche, entre -0.4 et 1
b = 0.33 #inverse de la pente entre 3 et 10
D = 8192 #voir commentaire plus bas
W = 10

#ID 3.6 : D = 512, W = 46
#ID 7 : D = 1024, W = 8
#ID 9.6 : D = 8192, W = 10

fig, axs = plt.subplots(1, 2)

for i in range(6) :

	errorRates = numpy.linspace(0, 0.5, 100)  #différents taux d'erreur, en vrai taux d'erreur max 20%, passer en échelle log
	penalite = 0.6 + 0.3*i #temps de pénalité en secondes

	MT = [ a + b * numpy.log2(1 + (D * numpy.sqrt(2) * scipy.special.erfinv(1-e)) / (2.066 * W))+ e*penalite
	   for e in errorRates ]

	for ax in axs :
		ax.plot(errorRates, MT, label="P : "+ str(round(penalite, 1)) + "s")

for ax in axs :
	ax.set_xlabel("error rate")
	ax.set_ylabel("movement time")
	ax.legend()

axs[1].set_ylim([3.2, 3.5])
axs[1].set_xlim([0, 0.25])
plt.tight_layout()
plt.ion()
plt.show(block=True)

#lancer quelques tests en changeant les paramètres et expliquer
#comportement du temps moyen quand epsilon tend vers 1 ; voir si calcul possible

	
