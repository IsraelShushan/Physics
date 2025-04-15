import numpy as np
import matplotlib.pyplot as plt
import copy
def collision(v1, v2, alpha):
 R = np.array([[np.cos(alpha), -np.sin(alpha)],
 [np.sin(alpha), np.cos(alpha)]])
 R_reverse = np.linalg.inv(R)
 v1_turned = np.dot(R, v1)
 v2_turned = np.dot(R, v2)
 
 # after rotate the x to be parallel to the contact line
 # rotate the velocities angle in alpha counterclockwise
 # using Shimur tenad and Shimur enrgia equations, we get
 # u1x = v2x
 # u2x = v1x
 # no collision on the y-axis so
 # u1y = v1y
 # u2y = v2y
 u1_turned = np.array([v2_turned[0], v1_turned[1]])
 u2_turned = np.array([v1_turned[0], v2_turned[1]])
 
 # now let's rotate the velocities vectors back
 u1 = np.dot(R_reverse, u1_turned)
 u2 = np.dot(R_reverse, u2_turned)
 
 return u1, u2
# constants
N=2000
start_velocity = 100
# Initialize velocities before concatenation
v1_before = np.zeros((N//2, 2))
v2_before = np.zeros((N//2, 2))
# Set velocities for group 1
v1_before[:, 0] = start_velocity
v1_before[:, 1] = 0
# Set velocities for group 2
v2_before[:, 0] = -start_velocity
v2_before[:, 1] = 0
# unite velocities
velocities_before = np.concatenate((v1_before, v2_before))
velocities_to_show_in_graph = []
velocities_to_show_in_graph.append(velocities_before[:, 0].copy())
graph_list.append(copy.copy(plt.gcf()))
for step in range(100):
 # Create new arrays of u1 and u2
 u1 = np.zeros((N // 2, 2))
 u2 = np.zeros((N // 2, 2))
 
 # Create random array of alpha
 angles = np.random.default_rng().uniform(0, np.pi / 2, N // 2)
 
 # In loop, calculate the velocity after collision
 for j in range(N // 2):
 u1[j], u2[j] = collision(v1_before[j], v2_before[j], angles[j])
 # shuffle one of the results
 u1_shuffled = np.random.default_rng().permutation(u1)
 #unite the arries
 velocities_after = np.concatenate((u1_shuffled, u2))
 #save u1 and u2 as velocites before for the next iteration
 v1_before = u1_shuffled
 v2_before =u2
 
 # save each histogram grapg of the ux velocity we got in result
 # Save tt he array of ux
 velocities_to_show_in_graph.append(velocities_after[:, 0].copy())
 
#show the last graph and the first graph
# Show the histogram of the first array of velocities
# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
# Show the histogram of the first array of velocities
axs[0].hist(velocities_to_show_in_graph[0], bins=50, alpha=0.7, color='blue', 
edgecolor='black',density=True)
axs[0].set_title('Histogram of Before Collision (Step 0)')
axs[0].set_xlabel('Velocity')
axs[0].set_ylabel('Frequency')
# Show the histogram of the last array of velocities
axs[1].hist(velocities_to_show_in_graph[-1], bins=50, alpha=0.7, color='blue', 
edgecolor='black',density=True)
axs[1].set_title(f'Histogram After Collision (Step 
{len(velocities_to_show_in_graph)})')
axs[1].set_xlabel('Velocity')
axs[1].set_ylabel('Frequency')
# Adjust layout for better spacing
plt.tight_layout()
# Show the figure
plt.show()