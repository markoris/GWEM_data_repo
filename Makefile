######################
### Group Commands ###
######################

all_plots:
	$(MAKE) plot_corner_ejecta
	$(MAKE) plot_corner_ejecta_fixed_f_disk
	$(MAKE) plot_corner_ejecta_narrow_mc
	$(MAKE) plot_corner_ejecta_fix_vw
	$(MAKE) plot_corner_ejecta_narrow_mc_fix_vw
	$(MAKE) plot_corner_binary
	$(MAKE) plot_corner_binary_fixed_f_disk
	$(MAKE) plot_corner_binary_narrow_mc
	$(MAKE) plot_corner_binary_fix_vw
	$(MAKE) plot_corner_binary_narrow_mc_fix_vw

plot_corner_ejecta_fixed_f_disk: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_0p3/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_Nedora21_grizyJHK_sigma_fit.dat --params md mw vd theta --outfile figures/corner_ejecta_fixed_f_disk.pdf

plot_corner_ejecta_narrow_mc_fix_vw_narrow_fdisk: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat --params md mw vd theta --outfile figures/corner_ejecta_narrow_mc_fix_vw_narrow_fdisk.pdf

plot_corner_ejecta_fixed_f_disk_narrow_mc_fix_vw: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_0p3_narrow_mc_fix_vw/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3_narrow_mc_fix_vw/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3_narrow_mc_fix_vw/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3_narrow_mc_fix_vw/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3_narrow_mc_fix_vw/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3_narrow_mc_fix_vw/samples_Nedora21_grizyJHK_sigma_fit.dat --params md mw vd theta --outfile figures/corner_ejecta_fixed_f_disk_narrow_mc_fix_vw.pdf

plot_corner_binary_fixed_f_disk: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_0p3/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_0p3/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_0p3/samples_Nedora21_grizyJHK_sigma_fit.dat --params mc delta_mc R14 log_alpha_dyn log_f_disk s1z s2z sigma_sys --outfile figures/corner_binary_fixed_f_disk.pdf

plot_corner_binary_narrow_mc_fix_vw_narrow_fdisk: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat --params mc delta_mc R14 log_alpha_dyn log_f_disk beta_phi sigma_sys --outfile figures/corner_binary_narrow_mc_fix_vw_narrow_fdisk.pdf

plot_corner_binary_narrow_mc_fix_vw_narrow_fdisk_nobetaphi: plot_corner.py
	python plot_corner.py --sample-files samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_Nedora21_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_KruFo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_DiCo20_grizyJHK_sigma_fit.dat samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk_nobf/samples_Nedora21_grizyJHK_sigma_fit.dat --params mc delta_mc R14 log_alpha_dyn log_f_disk --outfile figures/corner_binary_narrow_mc_fix_vw_narrow_fdisk_nobf.pdf

plot_lc_em: plot_lc.py
	python plot_lc.py --sample-files samples/EM_logfdisk_unconstrained/samples_KruFo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained/samples_DiCo20_grizyJHK_sigma_fit.dat samples/EM_logfdisk_unconstrained/samples_Nedora21_grizyJHK_sigma_fit.dat --params md vd mw vw theta --outname lc_em.pdf

plot_lc_gwem: plot_lc.py plot_lc_diff.py
	$(MAKE) plot_lc_gwem_Nedora
	$(MAKE) plot_lc_gwem_KruFo
	python plot_lc_diff.py
	rm samples_Nedora21_grizyJHK_sigma_fit_lcdata.dat samples_KruFo20_grizyJHK_sigma_fit_lcdata.dat 

plot_lc_gwem_Nedora: plot_lc.py
	python plot_lc.py --sample-files samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat --params md vd mw vw theta --outname lc_gwem_Nedora_narrow_mc_fix_vw_narrow_fdisk.pdf --save-lc-data

plot_lc_gwem_KruFo: plot_lc.py
	python plot_lc.py --sample-files samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat --params md vd mw vw theta --outname lc_gwem_KruFo_narrow_mc_fix_vw_narrow_fdisk.pdf --save-lc-data

plot_lc_gwem_fixed_f_disk: plot_lc.py
	python plot_lc.py --sample-files samples/GW+EM_logfdisk_0p3_narrow_mc_fix_vw/samples_Nedora21_grizyJHK_sigma_fit.dat --params md vd mw vw theta --outname lc_gwem_fixed_f_disk_narrow_mc_fix_vw.pdf

overplot_fits_likelihood_data:
	
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat DiCo20_converted_posteriors.dat
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat KruFo20_converted_posteriors.dat
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat Nedora21_converted_posteriors.dat
	python ~/rift/MonteCarloMarginalizeCode/Code/bin/plot_posterior_corner.py --parameter mc --parameter q --parameter xi --parameter LambdaTilde --parameter-log-scale LambdaTilde --composite-file all.net_moreLt --use-legend --quantiles [0.9] --lnL-cut 15 --use-all-composite-but-grayscale --flag-tides-in-composite --bind-param mc --param-bound [1.1972,1.1982] --bind-param q --param-bound [0.5,1] --bind-param xi --param-bound [0,0.05] --bind-param LambdaTilde --param-bound [2,7] --publication --posterior-file DiCo20_converted_posteriors.dat --posterior-color red --posterior-label DiCo20 --posterior-file KruFo20_converted_posteriors.dat --posterior-label KruFo20 --posterior-color black --posterior-file Nedora21_converted_posteriors.dat --posterior-color blue --posterior-label Nedora21
	mv corner_mc_q_xi_LambdaTilde.png figures/fits_likelihood.png
	
overplot_fits_likelihood_data_nobf:
	
	python convert_coordinates_for_overplotting.py samples/samples_no_beta_phi/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat DiCo20_converted_posteriors.dat
	python convert_coordinates_for_overplotting.py samples/samples_no_beta_phi/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat KruFo20_converted_posteriors.dat
	python convert_coordinates_for_overplotting.py samples/samples_no_beta_phi/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat
	mv converted_posteriors.dat Nedora21_converted_posteriors.dat
	python ~/rift/MonteCarloMarginalizeCode/Code/bin/plot_posterior_corner.py --parameter mc --parameter q --parameter xi --parameter LambdaTilde --parameter-log-scale LambdaTilde --composite-file all.net_moreLt --use-legend --quantiles [0.9] --lnL-cut 15 --use-all-composite-but-grayscale --flag-tides-in-composite --bind-param mc --param-bound [1.1972,1.1982] --bind-param q --param-bound [0.5,1] --bind-param xi --param-bound [0,0.05] --bind-param LambdaTilde --param-bound [2,5] --publication --posterior-file DiCo20_converted_posteriors.dat --posterior-color red --posterior-label DiCo20 --posterior-file KruFo20_converted_posteriors.dat --posterior-label KruFo20 --posterior-color black --posterior-file Nedora21_converted_posteriors.dat --posterior-color blue --posterior-label Nedora21
	mv corner_mc_q_xi_LambdaTilde.png figures/fits_likelihood_nobf.png

overplot_DiCo20_likelihood_data:
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_DiCo20_grizyJHK_sigma_fit.dat
	python ~/rift/MonteCarloMarginalizeCode/Code/bin/plot_posterior_corner.py --parameter mc --parameter q --parameter xi --parameter LambdaTilde --composite-file all.net_combined --use-legend --quantiles None --lnL-cut 15 --use-all-composite-but-grayscale --flag-tides-in-composite --posterior-file converted_posteriors.dat --bind-param q --param-bound [0.5,1] --bind-param xi --param-bound [0,0.05] --bind-param LambdaTilde --param-bound [0,10000] --publication

overplot_KruF20_likelihood_data:
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_KruFo20_grizyJHK_sigma_fit.dat
	python ~/rift/MonteCarloMarginalizeCode/Code/bin/plot_posterior_corner.py --parameter mc --parameter q --parameter xi --parameter LambdaTilde --composite-file all.net_combined --use-legend --quantiles None --lnL-cut 15 --use-all-composite-but-grayscale --flag-tides-in-composite --posterior-file converted_posteriors.dat --bind-param q --param-bound [0.5,1] --bind-param xi --param-bound [0,0.05] --bind-param LambdaTilde --param-bound [0,10000] --publication

overplot_Nedora21_likelihood_data:
	python convert_coordinates_for_overplotting.py samples/GW+EM_logfdisk_unconstrained_narrow_mc_fix_vw_narrow_fdisk/samples_Nedora21_grizyJHK_sigma_fit.dat
	python ~/rift/MonteCarloMarginalizeCode/Code/bin/plot_posterior_corner.py --parameter mc --parameter q --parameter xi --parameter LambdaTilde --composite-file all.net_combined --use-legend --quantiles None --lnL-cut 15 --use-all-composite-but-grayscale --flag-tides-in-composite --posterior-file converted_posteriors.dat --bind-param q --param-bound [0.5,1] --bind-param xi --param-bound [0,0.05] --bind-param LambdaTilde --param-bound [0,10000] --publication

