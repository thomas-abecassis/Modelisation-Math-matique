import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

#
# On prépare les trois matrices à empiler



blanc = 255 * np.ones((10, 10), dtype = np.uint8)
noir =  np.zeros((10, 10), dtype = np.uint8)


# On empile les trois matrices
carreBlanc = np.stack((blanc, blanc, blanc), axis = 2)
carreNoir = np.stack((noir,noir,noir), axis = 2)

ligne1= np.block([[carreBlanc],[carreNoir]]) 
ligne1= np.block([[ligne1],[ligne1]])
ligne1= np.block([[ligne1],[ligne1]])

ligne2= np.block([[carreNoir],[carreBlanc]])
ligne2= np.block([[ligne2],[ligne2]])
ligne2= np.block([[ligne2],[ligne2]])

echiquier=np.vstack((ligne1,ligne2))
echiquier=np.vstack((echiquier,echiquier))
echiquier=np.vstack((echiquier,echiquier))

#print([carres]*carres)

# visualisation avec imshow
plt.imshow(echiquier)
#plt.show() # inutile en interactif
#
# Sauvegarde avec imsave
mpg.imsave('carres4.png', echiquier)
