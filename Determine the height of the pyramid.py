"""
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The figure illustrates the rule used by the builders:

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
"""

# create user input:
blocks = int(input())

# set height layer to start at 0:
height = 0

# create while loop:
while blocks:
    # set first condition: block equation:
    blocks = blocks - height
    # set second condition:
    if blocks == 0:
        # break
        break
    # set third condition:
    elif blocks <= height:
        # break
        break
    else:
        # else add a layer each time to height:
        height +=1
# print the number of fully completed layers:
print("The height of the pyramid: ",height)