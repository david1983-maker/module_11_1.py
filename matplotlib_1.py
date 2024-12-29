import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=24)
ax.set_ylabel('Square of Value', fontsize=24)
ax.tick_params(axis = 'both', labelsize=14)



plt.show()