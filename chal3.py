import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

#
# On prépare les trois matrices à empiler



R = 255 * np.ones((10, 100), dtype = np.uint8)
V = 255 * np.ones((10, 100), dtype = np.uint8)
B = 255 * np.ones((10, 100), dtype = np.uint8)

test=np.linspace(1,256,60*256,dtype=np.uint8)
test=test.reshape((256,60))
test=np.rot90(test,-1)


# On empile les trois matrices
carres = np.stack((test, test, test), axis = 2)

#print([carres]*carres)

# visualisation avec imshow
plt.imshow(carres)
#plt.show() # inutile en interactif
#
# Sauvegarde avec imsave
mpg.imsave('carres3.png', carres)
