import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg
import os

# On prepare les trois matrices a empiler
R =255* np.ones((50), dtype=np.uint8) - 255* np.eye((50), dtype=np.uint8)
V =255* np.ones((50), dtype=np.uint8) - 255* np.eye((50), dtype=np.uint8)
B =255* np.ones((50), dtype=np.uint8) -  255* np.eye((50), dtype=np.uint8)

# Pour l'instant, la superposition donnerait du blanc.# On mets a 0 les 100 premieres lignes de chacune des matrices

print(R)
# On empile les trois matrice
carres = np.stack((R, V, B), axis =2)


os.chdir("../")

# visualisation avec imshow
plt.imshow(carres)
plt.show() # inutile en interactif

# Sauvegarde avec imsave
mpg.imsave('carres.png', carres)