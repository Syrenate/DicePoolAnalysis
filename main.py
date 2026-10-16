import matplotlib.pyplot as plt
import numpy as np

from analysis import ChanceOfSucess
from matplotlib.widgets import TextBox

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

def plt_render(dice_pool):
    ax.cla()
    if dice_pool != []:
        x = np.linspace(1, max(dice_pool), max(dice_pool)) 
        y_plots = []
        for total_target in range(1,len(dice_pool)+1):
            y = []
            for x_val in x:
                y.append(ChanceOfSucess(dice_pool, x_val, total_target))
            y_plots.append((total_target, y))

        for target, y in y_plots:
            ax.plot(x,y,'o-',linewidth=2,label=f"Dice needed: {target}")
            ax.set(xlim=(1,max(dice_pool)), ylim=(0,1))

    ax.set_title("Probability of Success against Dice Target Values")
    ax.set_xlabel("Dice Target Value")
    ax.set_ylabel("Probability of Success")

    ax.grid()
    ax.legend()
    
def submit(pool):
    dice_pool = []
    try:
        dice_pool = list(map(lambda x: int(x), pool.split(',')))
    except:
        return 0

    plt_render(dice_pool)
    fig.canvas.draw_idle()

axbox = fig.add_axes((0.1, 0.05, 0.8, 0.075))
text_box = TextBox(axbox, "Dice Pool", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("6,6,6,4,4")

plt_render([6,6,6,4,4])
plt.show()
