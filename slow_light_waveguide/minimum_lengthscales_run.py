import numpy as np
import os
import imageruler

path = './'
files = os.listdir(path)
files.sort()
print('Design file, solid minimum lengthscale (a), void minimum lengthscale (a), minimum lengthscale (a)')

design_size = (1, 10.2)

for file_name in ['Design_Dnum_2.csv', 'HigRes_DesMatch_Opt_Dnum_2.csv']:  
    design_pattern = np.loadtxt(path+file_name, delimiter=',')

    solid_mls, void_mls = imageruler.minimum_length_scale(design_pattern, periodic=(True, True))
    print(file_name, solid_mls, void_mls, min(solid_mls, void_mls))
