import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


temperatures = np.array((1125, 1053, 1001, 838))    # K
k_values = np.array((11.59, 1.67, 0.380, 0.0011))   # L / (mol.s)
k_errors = np.array((1E-2, 1E-2, 1E-3, 1E-5))

# plot config
params = {
    'lines.linewidth': 2.0,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.autolayout': True,
    'figure.titlesize': 18,
    'figure.figsize': (12, 6),
    'legend.shadow': False,
    'legend.fontsize': 14,
}

plt.rcParams.update(params)

# data points
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1.errorbar(temperatures, k_values, yerr=k_errors, marker='o', linestyle='')
ax2.scatter(1/temperatures, np.log(k_values), label='Data')

# regression
slope, intercept, r_value, p_value, std_err = linregress(
    1/temperatures, np.log(k_values))
regression = slope * 1/temperatures + intercept
ax2.plot(1/temperatures, regression,
         color='red', alpha=0.5,
         label=r'$\ln k={:.0f}\frac{{1}}{{T}}+{:.2f}$'.format(slope, intercept))
ax2.legend()

# visuals
for ax in (ax1, ax2):
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    ax.xaxis.major.formatter._useMathText = True
    ax.figure.canvas.draw()
    order_magnitude = ax.xaxis.get_offset_text().get_text().replace('\\times', '')
    ax.xaxis.offsetText.set_visible(False)
    if ax == ax1:
        ax.set_xlabel(r'$T$ / ' + order_magnitude + ' $K$', )
        ax.set_ylabel(r'$k / \frac{\ell}{mol \cdot s}$')
        ax.set_title('Forma exponencial', color='dimgray')
    else:
        ax.set_xlabel(r'$\frac{1}{T}$ / ' + order_magnitude + ' $K^{-1}$', )
        ax.set_ylabel(r'$\ln k$')
        ax.set_title('Forma linearizada', color='dimgray')

plt.suptitle('Gráficos para a equação de Arrhenius',
             color='dimgray')
plt.show()
