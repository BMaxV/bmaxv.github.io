#regular wfc applies a fixed pattern.

#what i want with a continnuous method, is that
# and existing state influences based on weights, chancd and area
# so a pattern
a="""
iii
ooo
kkk
"""

# creates a weight of 3 at 0,1 for i
# a weight of 3 for k at 0,-1
# when the weigh of the situation matches the weight of tje pattern, apply the pattern or increase the chance for the center piece.

#and i suppose it starts by counting rhe weights of tje situation.

for position, value in situation:
    if value!= None:
        #neighbors?
