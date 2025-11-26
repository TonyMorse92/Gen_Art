import numpy as np
import matplotlib.pyplot as plt 
import random

rng = np.random.RandomState(5)
data = rng.randint(0, 2, 500)

#print(f"Data: {data}")
#print(f"Roll data: {np.roll(data, 1)}")

rules = np.random.randint(0, 128, 128)
rule_number = np.random.choice(rules)
rule_string = np.binary_repr(rule_number, 8)
rule = np.array([int(bit) for bit in rule_string])

#print(f"Rule: {rule}")

# Add a comment here. I always blank when I come back after a couple days
# Just think about a grid 
def rule_index(state):
	left_neighbor, cell, right_neighbor = state
	index = 7 - (4*left_neighbor + 2*cell + right_neighbor)
	return int(index)


all_trip = np.stack([np.roll(data, 1),
	data,
	np.roll(data, -1)]
)

# Initialize array that will be loded by matplotlib
binary_data = np.array(data, dtype=int)
binary_data = binary_data[np.newaxis, :]

# Run the rule a bunch of times
cnt = 0
while cnt < 300:
	data = rule[np.apply_along_axis(rule_index, 0, all_trip)]
	all_trip = np.stack([np.roll(data, 1),
		data,
		np.roll(data, -1)]
	)
	data = data[np.newaxis, :]
	binary_data = np.concatenate((binary_data, data), axis=0)
	cnt+=1

# Plot the result
plt.imshow(binary_data, cmap='Greys')
plt.axis("off")
plt.title(f"Cellular Automata Rule {rule_string} ({rule_number})")
plt.show()
