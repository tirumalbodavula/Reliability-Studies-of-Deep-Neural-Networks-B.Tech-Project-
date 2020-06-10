import numpy as np
import matplotlib.pyplot as plt


N = 4
Wrong_classified = (7092, 6484, 6961, 6960)
Correctly_classified = (408, 1016, 539, 540)
menStd = (2, 3, 4, 1)
womenStd = (3, 5, 2, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, Wrong_classified, width, yerr=menStd)
p2 = plt.bar(ind, Correctly_classified, width,
             bottom=Wrong_classified, yerr=womenStd)

plt.ylabel('ImageNet-A')
plt.title('Classification of Images by Neural Network Models')
plt.xticks(ind, ('VGG16', 'Inception-v3', 'ResNet-50', 'MobileNet'))
plt.yticks(np.arange(0, 8000, 500))
plt.legend((p1[0], p2[0]), ('Wrongly_Classified_Images','Correctly_Classified_Images'))

plt.show()