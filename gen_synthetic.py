# Copyright © 2024 by Northwestern University. All Rights Reserved

import os
import numpy as np
import random
from skimage.draw import ellipse
from skimage import io
from datetime import datetime

def gen_good(n, savedir):
    for i in range(n):
        img = np.zeros((dim, dim), dtype=np.uint8)
        x = random.randint(dim/4, (dim/4*3))
        y = random.randint(dim/4, (dim/4*3))
        rad1 = random.randint(np.ceil(dim*.05),np.ceil(dim*0.25))
        rad2 = random.randint(np.ceil(dim*.05),np.ceil(dim*0.25))
        rot = random.randint(0,180)
        rr, cc = ellipse(x, y, rad1, rad2, rotation=np.deg2rad(rot))
        img[rr, cc] = random.randint(255,255)
        nowstr = datetime.now().strftime('%H-%M-%S_%Y-%m-%d') #nb odd format for easier searching
        savename = savedir + '/' + 'good_' + nowstr + '_' + str(i) + '.jpeg'
        io.imsave(savename, img)

def gen_bad(n, max_part, savedir):
    # if completely overlapping, don't save
    num_overlap = 0
    for i in range(n):
        parts = random.randint(2,max_part)       
        img = np.zeros((dim, dim), dtype=np.uint8)
        overlap = 0
        for j in range(parts):
            start = img.copy()
            x = random.randint(dim/4, (dim/4*3))
            y = random.randint(dim/4, (dim/4*3))
            rad1 = random.randint(np.ceil(dim*.01),np.ceil(dim*0.20))
            rad2 = random.randint(np.ceil(dim*.01),np.ceil(dim*0.20))
            rot = random.randint(0,180)
            rr, cc = ellipse(x, y, rad1, rad2, rotation=np.deg2rad(rot))
            img[rr, cc] = random.randint(255,255)
            if np.array_equal(start, img):
                overlap = 1
                num_overlap = num_overlap+1
                break 
            if not overlap:
                nowstr = datetime.now().strftime('%H-%M-%S_%Y-%m-%d') #nb odd format for easier searching
                savename = savedir + '/' + 'bad_' + nowstr + '_' + str(i) + '.jpeg'
                io.imsave(savename, img)

### Update the options below ###
dim = 64
# folder = # add directory path name here, no trailing slash
gen_good(10, savedir=folder)
gen_bad(10, max_part=2, savedir=folder)
