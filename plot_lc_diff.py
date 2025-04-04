import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', size = 40)
plt.rc('lines', lw=4)
colors = {"g": "blue", "r": "cyan", "i": "lime", "z": "green", "y": "greenyellow", "J": "gold",
         "H": "orange", "K": "red", "S": "darkred"}

bands = 'grizyJHK'
times = np.load('Kilonova-Neural-Network/times.npy')
lc_Nedora21 = np.loadtxt('samples_Nedora21_grizyJHK_sigma_fit_lcdata.dat')
lc_KruFo20 = np.loadtxt('samples_KruFo20_grizyJHK_sigma_fit_lcdata.dat')

plt.figure(figsize=(19.2, 10.8))

for band in bands:
	lc_diff = lc_Nedora21[bands.index(band)] - lc_KruFo20[bands.index(band)] 
	plt.plot(times, lc_diff, color=colors[band], alpha=0.3, label='%s' % (band))

import itertools
from matplotlib import ticker

def flip(items, ncol):
    '''
    credit to Avaris on StackOverflow for this function
    '''
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])

plt.xscale('log')
plt.gca().set_xticks([0.125, 0.5, 1, 2, 4, 8, 16, 32, 64])
plt.gca().get_xaxis().set_major_formatter(ticker.FormatStrFormatter('%g'))
plt.xlabel(r"$t$ (days)", labelpad=-5)
plt.ylabel("AB Mag")
#plt.gca().set_ylim(top=35)
plt.gca().invert_yaxis()
handles, labels = plt.gca().get_legend_handles_labels()
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(flip(handles, 2), flip(labels, 2), ncol=2, loc='lower left', fontsize=30)

#plt.savefig('figures/lc_%s.pdf' % '_'.join(sample_file.split('.')[0].split('/')[-1].split('_')[1:]))
plt.savefig('figures/lc_diff.pdf')
plt.close()
