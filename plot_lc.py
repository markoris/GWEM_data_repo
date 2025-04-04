import matplotlib.pyplot as plt
import numpy as np
import argparse
import torch
import torch.nn as nn
import os, sys
os.environ["OMP_NUM_THREADS"] = "20"
sys.path.append('/home/marko.ristic/RIT-matters/communications/20230901-YingleiMarko-AutoencoderPE/Kilonova-Neural-Network')
from KilonovaInterpolator import VAE, Encoder, Decoder, DataProcessor
import corner

parser = argparse.ArgumentParser()
parser.add_argument('--sample-files', help='Files containing samples for light-curve plot', nargs='+')
parser.add_argument('--params', help='Which parameters to plot', nargs='+')
parser.add_argument('--outname', help='Output file name')
parser.add_argument('--save-lc-data', action='store_true')
args = parser.parse_args()

#if 'GW+EM' in args.sample_files[0]: outname = 'gwem'
#else: outname = 'em'

bands = 'grizyJHK'
color_list=['black', 'red', 'blue', 'green']
plt.rc('font', size=30)

# load the samples

cwd = os.getcwd()
os.chdir('Kilonova-Neural-Network')

times = np.load('times.npy')

vaes = {'g': torch.load('AE_g_real_angle_logm.pt'),
	'r': torch.load('AE_r_real_angle_logm.pt'),
	'i': torch.load('AE_i_real_angle_logm.pt'),
	'z': torch.load('AE_z_real_angle_logm.pt'),
	'y': torch.load('AE_y_real_angle_logm.pt'),
	'J': torch.load('AE_J_real_angle_logm.pt'),
	'H': torch.load('AE_H_real_angle_logm.pt'),
	'K': torch.load('AE_K_real_angle_logm.pt'),
	}

os.chdir(cwd)

# Load data used in EM_PE for consistency

data = {'g': np.loadtxt('AT2017gfo_data/g.txt'),
	'r': np.loadtxt('AT2017gfo_data/r.txt'),
	'i': np.loadtxt('AT2017gfo_data/i.txt'),
	'z': np.loadtxt('AT2017gfo_data/z.txt'),
	'y': np.loadtxt('AT2017gfo_data/y.txt'),
	'J': np.loadtxt('AT2017gfo_data/J.txt'),
	'H': np.loadtxt('AT2017gfo_data/H.txt'),
	'K': np.loadtxt('AT2017gfo_data/K.txt'),
	}

plt.rc('font', size = 40)
plt.rc('lines', lw=4)
colors = {"g": "blue", "r": "cyan", "i": "lime", "z": "green", "y": "greenyellow", "J": "gold",
         "H": "orange", "K": "red", "S": "darkred"}

for sample_file in args.sample_files:
	print(sample_file)
	samples = np.genfromtxt(sample_file, names=True)

	param_samples = np.array([np.log10(samples[param]) if param == 'md' or param == 'mw' else samples[param] for param in args.params]).T
	print('Sample array dimensions for %s: ' % sample_file, param_samples.shape)
	
	lnL = samples['lnL']
	lnp = samples['lnp']
	lnps = samples['lnps']
	weights = samples['weights']
	weights /= weights.sum()
	
	quantiles = [0.16, 0.50, 0.84]

	# find the quantiles

	lc_params = np.array([[corner.core.quantile(param_samples[:, j], quantiles[i], weights=weights) for i in range(len(quantiles))] for j in range(param_samples.shape[1])])[:, :, 0]
	print(lc_params)
	lc_params = DataProcessor().to_torch_tensor(lc_params)[0]
	lc_params = lc_params.T
	
	plt.figure(figsize=(19.2, 10.8))
	counter = 7

	for band in bands:
		lcs, _, _ = vaes[band](lc_params)
		try:
			lc_array = np.concatenate((lc_array, lcs[1].detach().cpu().numpy()[None, :]), axis=0)
		except NameError:
			lc_array = lcs[1].detach().cpu().numpy()[None, :]
		lcs = lcs.detach().numpy() + 5*np.log10(40e6)-5
		plt.plot(times, lcs[1]+counter, color=colors[band], alpha=0.3, label='%s + %d' % (band, counter))
		sigma_stat_upp = lcs[1]-lcs[2]
		sigma_stat_low = lcs[0]-lcs[1]
		#print('sigma stat: ', sigma_stat_upp.mean(), sigma_stat_low.mean())
		sigma_upp = np.sqrt(sigma_stat_upp**2 + 0.5**2) 
		sigma_low = np.sqrt(sigma_stat_low**2 + 0.5**2)
		#print('sigma upp: ', sigma_upp.mean()) 
		#print('sigma low: ', sigma_low.mean()) 
		plt.fill_between(times, lcs[1]-sigma_low+counter, lcs[1]+sigma_upp+counter, color=colors[band], alpha=0.3)
		plt.scatter(data[band][:, 0], data[band][:, 2]+counter, c=colors[band])
		counter -= 1

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
	plt.savefig('figures/%s' % args.outname)
	plt.close()

	print(lc_array.shape)
	
	if args.save_lc_data == True:
		np.savetxt(os.path.basename(sample_file)[:-4]+'_lcdata.dat', lc_array)

# keep the samples which fall between the quantiles

# plot median and fill-between for quantiles
