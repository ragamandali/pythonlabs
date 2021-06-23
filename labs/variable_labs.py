"""
title: variable_labs
author: raga mandali
date: 06/21/2021
"""

import math

#Swallow Exercise
#How many grams total a single swallow is capable of carrying -- 60/3
swallow_limit = 60/3 

#How many swallows it will take to carry a coconut weighing 1450 grams -- 1450/(60/3) = 72.5
coconut_swallows = 1450/swallow_limit 

print("The number of swallows it requires to carry a coconut is " + str(math.ceil(coconut_swallows)))


#Macaw Exercise
coconut_weight = 1450
macaw_weight = 900

macaw_limit = macaw_weight/3 #300.0

macaws_required = coconut_weight/macaw_limit #4.8333

print("The number of macaws required to carry a coconut is " + str(math.ceil(macaws_required)))