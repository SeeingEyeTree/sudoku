import cv2
import numpy as np
def match_templat(where,what,threshold,test=False):
    res = cv2.matchTemplate(where,what,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    if test:
	    whereRGB=cv2.cvtColor(where,cv2.COLOR_GRAY2RGB)
	    w1, h1 = what.shape[::-1]
	    for pt1 in zip(*loc[::-1]):
	            cv2.rectangle(whereRGB, pt1, (pt1[0] + w1, pt1[1] + h1), (0,0,255), 2)
	    cv2.imshow('matches',whereRGB)
	    print(loc)
    y=loc[1]
    x=loc[0]
    return x,y

