import numpy as np
from classifiers import *

classifier = Meso4()
print(classifier.predict(np.zeros((10, 256, 256, 3))))