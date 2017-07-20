import random

middle = ["And I see how trees survive", "July is funny and cool", "Waves crash on the sandy shore", "Looking up at their branches", "and twenty haikus began", "wondered, 'will i enjoy it?'", "Through fellow blogs inspired my", "What did you think of this trip?", "They were fully hooked before"]
start = ["Sand scatters the beach", "Between the two trees", "My journey of nine", "Along the way I", "an enchanting trip", "Now, readers, tell me", "Earn their attention!"]
end = ["Blue water shimmers", "Which one should we climb?", "with a leap of faith", "Will I see it through?", "Flights of fantasy", "Was the trek worth it?", "They ever met you!"]

num = random.randrange(0,7,1)
n = random.randrange(0,8,1)
m = random.randrange(0,7,1)

print (start[num])
print (middle[n])
print (end[m])
