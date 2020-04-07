#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sanithps98
"""

import pandas as pd
import numpy as np
import numpy_financial as npf

project1_cf = pd.DataFrame({"Year":np.arange(0,6),"cf": [-800,200,250,300,350,400]})
print(project1_cf)

##    Year   cf
## 0     0 -800
## 1     1  200
## 2     2  250
## 3     3  300
## 4     4  350
## 5     5  400


project2_cf = pd.DataFrame({"Year":np.arange(0,6),"cf": [-500,150,170,178,250,300]})
print(project2_cf)

##    Year   cf
## 0     0 -500
## 1     1  150
## 2     2  170
## 3     3  178
## 4     4  250
## 5     5  300

irr1 = npf.irr(project1_cf["cf"])
irr2 = npf.irr(project2_cf["cf"])


irr_df = pd.DataFrame({"Name":["Project1", "Project2"],"IRR":[irr1, irr2]})
print(irr_df)
                  

##        Name       IRR
## 0  Project1  0.221603
## 1  Project2  0.267620

'''
From the above table we can see that project 1 has an IRR of 22.16% and project 2 has an IRR of 26.76. 
Even though project 1 offers higher cash flows, project 1 has a lower internal rate of returns. 
If the managers goal is to choose the project that maximizes profitability then he/she should choose project 2.
'''
