#answer always in boolean

physics = 67
chemistry = 19

print (physics > 33 and chemistry >> 33) # both should be true
print (physics > 33 or chemistry >> 33) # one should be true
#not simply reverses the value
print(not physics > 33)
print (not (physics > 33 or chemistry >> 33))