#create animation video that present a ball that thrown in v0= (4,5)m/s
#and his move only affected by the w=mg power. 
#the video present a parabolic movement of the ball
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches
v0x=4
v0y=5
g=10
t=np.linspace(0,1,num=300,dtype=np.double)
x=v0x*t
y=v0y*t-0.5*g*t**2
fig, ax = plt.subplots(nrows=1,ncols=1)
ax.set_xlim(0, 5), ax.set_xticks([])
ax.set_ylim(0, 1.5), ax.set_yticks([])
ax.plot(x,y,'g--')
dot = ax.scatter(x[0],y[0] )
arw=mpatches.FancyArrow(0, 0, x[0], y[0],width=0.005,head_width=0.1,length_includes_head=True,overhang=1)
ax.add_patch(arw)
def update(frame_number):
    dot.set_offsets([x[frame_number], y[frame_number]])           
    arw.set_data(dx=x[frame_number])
    arw.set_data(dy=y[frame_number])
# Construct the animation, using the update function as the animation director

animation = FuncAnimation(fig, update, interval=10, save_count=300)
animation.save("q1.mp4")
#animation.save("q1.gif")