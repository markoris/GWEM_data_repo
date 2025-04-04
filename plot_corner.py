import argparse
import numpy as np
import corner
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--sample-files', help='Files containing samples for corner plot', nargs='+')
parser.add_argument('--params', help='Which parameters to plot', nargs='+')
parser.add_argument('--outfile', help='Output filename for corner plot')
parser.add_argument('--quantiles', action='store_true') 
args = parser.parse_args()

fig = plt.figure(figsize=(12.5, 12.5))
color_list=['black', 'red', 'blue']

counter = 0

label_dict = {'mc': r'$\mathcal{M}_c$',
        'delta_mc': r'$\delta$',
	     'R14': r'$R_{1.4}$',
    'log_alpha_dyn': r'$\log \alpha_{\rm{dyn}}$',
       'log_f_disk': r'$\log f_{\rm{disk}}$',
	 'beta_phi': r'$\beta_\phi$',
	      'a1z': r'$a_{1z}$',
	      'a2z': r'$a_{2z}$',
	  'chi_eff': r'$\chi_{\rm{eff}}$',
	'sigma_sys': r'$\sigma_{\rm{sys}}$',
 	       'md': r'$\log m_d$',
 	       'vd': r'$v_d$',
	       'mw': r'$\log m_w$',
	    'theta': r'$\theta$',
	       'vw': r'$v_w$'}

for sample_file in args.sample_files:
	samples = np.genfromtxt(sample_file, names=True)

	param_samples = np.array([np.log10(samples[param]) if param == 'md' or param == 'mw' else samples[param] for param in args.params]).T
	print('Sample array dimensions for %s: ' % sample_file, param_samples.shape)
	
	lnL = samples['lnL']
	lnp = samples['lnp']
	lnps = samples['lnps']
	weights = samples['weights']
	weights /= weights.sum()
	
	if args.quantiles: quantiles = [0.16, 0.50, 0.84]
	else: quantiles = None

	if 'GW' in sample_file: 
		ls = '-'
		lw = 1
	else: 
		ls = '--'
		lw = 1

#	if '0p3' in sample_file: contours = False
#	else: contours = True

	contours = True

	corner.corner(param_samples,
	weights=weights,
	labels=[label_dict[param] for param in args.params],
	fig=fig,
	titles=np.array([label_dict[param] for param in args.params]),
	quantiles=quantiles,
	title_quantiles=quantiles,
	show_titles=np.any(args.quantiles),
	plot_datapoints=False,
	plot_density=False,
	plot_contours=contours,
	smooth1d=0.1,
	smooth=0.1,
	color=color_list[counter%3],
	title_kwargs={"fontsize": 24-1.5*len(args.params)},
	label_kwargs={"fontsize": 24-1.5*len(args.params)},
	hist_kwargs={"linestyle": ls, "linewidth": lw},
	contour_kwargs={"linestyles": ls},
	title_fmt=".3f",
	verbose=False,
	levels=[0.9],
	)
	counter+=1

xcoord = 1.2 #len(params) - 1
ycoord = param_samples.shape[1]+0.3

# clean names for use in legend

legend_fits = [name.split('.')[0].split('/')[-1].split('_')[1] for name in args.sample_files]
legend_lnl = [name.split('.')[0].split('/')[1].split('_')[0] for name in args.sample_files]
legend_names = [fit+': '+lnl for fit, lnl in zip(legend_fits, legend_lnl)]

#legend_names = [name.split('.')[0].split('/')[-1].split('_')[1:5] for name in args.sample_files]
#for legend in legend_names: legend[-1] = legend[-1].replace('p', '.')
#legend_names = ['_'.join(name) for name in legend_names]

### generate the legend
lgd = plt.legend([name for name in legend_names], bbox_to_anchor=(xcoord, ycoord), loc='upper right', fontsize=25-len(args.params))
for i in range(len(args.sample_files)):
    #lgd.legendHandles[i].set_color(color_list[i%3])
    lgd.legend_handles[i].set_color(color_list[i%3])

for ax in fig.get_axes():
      ax.tick_params(axis='both', labelsize=25-2*len(args.params))
plt.savefig(args.outfile)
