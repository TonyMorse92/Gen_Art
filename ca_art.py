import numpy as np
import matplotlib.pyplot as plt 
import random

rng = np.random.RandomState(42)
data = rng.randint(0, 2, 20)

#print(f"Data: {data}")
#print(f"Roll data: {np.roll(data, 1)}")


rule_number = 30
rule_string = np.binary_repr(rule_number, 8)
rule = np.array([int(bit) for bit in rule_string])

#print(f"Rule: {rule}")

def rule_index(state):
	left_neighbor, cell, right_neighbor = state
	index = 7 - (4*left_neighbor + 2*cell + right_neighbor)
	return int(index)


all_trip = np.stack([
	np.roll(data, 1),
	data,
	np.roll(data, -1)]
)



new_data = rule[np.apply_along_axis(rule_index, 0, all_trip)]
#print(np.apply_along_axis(rule_index, 0, all_trip))
#print(f"New data: {new_data}")
#print("\n\n\n\n")
#print(all_trip)

### Try plotting the first few
binary_data = np.array([
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
])


dt = data[np.newaxis, :]

#binary_data = np.array(data, dtype=int)
binary_data = np.concatenate((binary_data, dt), axis=0)

plt.imshow(binary_data, cmap='Greys')
plt.axis("off")
plt.title("Cellular Automata")
plt.show()



