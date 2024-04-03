import numpy as np
import matplotlib.pyplot as plt

# Define the beta function
def beta(d, x):
    return d - 1 - (1 + np.exp(x)) * np.log(1 + np.exp(-x))

# Define x range
x = np.linspace(-10, 10, 400)

# Initialize the plot
plt.figure(figsize=(8, 6))

# Plot beta for d=3 and d=1
plt.plot(x, beta(3, x), label=r'$d=3$: metal-insulator transition')
plt.plot(x, beta(1, x), label=r'$d=1$: always localized')

# Plot modifications for d=2 case
plt.plot(x, beta(2, x) - 0.05, color='orange', linestyle='dashed', label=r'$d=2$: metal-insulator transition')
plt.plot(x, beta(2, x) + 0.5 * np.exp(-(x - 2)**2) + 0.1, color='orange', linestyle='dashed', label=r'$d=2$: always localized')

# # Adding arrows for RG flow
# for xi in [-3, 1, 3, 5, 7, 9]:
#     plt.arrow(xi, -3.5, 0, 1, head_width=0.2, head_length=0.2, fc='k', ec='k')

# Set plot range and frame
plt.xlim(-4, 10)
plt.ylim(-4, 2)
plt.gca().set_frame_on(True)

# Adding x and y axis in the middle
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel(r'$\ln(G)$', fontsize=14)
plt.ylabel(r'$\beta(G)=\frac{d\ln G}{d\ln L}$', fontsize=14)

# Remove ticks and add legend
plt.xticks([])
plt.yticks([])

plt.legend()

# Save the figure
plt.savefig("scaling_of_Anderson_localization.svg")
# plt.show()
