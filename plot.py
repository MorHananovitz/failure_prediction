import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def data(attr):
	
	for sn in attr.serial_numbers:
		plt.plot(sn.cycle, sn.measurement, 'o-', label=sn.name)

	plt.plot(plt.xlim(), [attr.lower_limit, attr.lower_limit], 'r--')
	plt.plot(plt.xlim(), [attr.upper_limit, attr.upper_limit], 'r--')

	plt.xlabel('CycleCount', fontsize=15)
	plt.ylabel('Measurement AVG', fontsize=15)

	plt.title(attr.name)
	plt.legend(numpoints=1, loc='best')
	plt.tick_params(axis='both', labelsize=15)
	plt.grid(color='lightgray', linestyle='--')

	plt.show()

def manual(attr, series_in, series_out, predictions_mean, predictions_std, lin, lout, c, s):
	
	sn = attr.serial_numbers[s]
	
	# plot the whole serial number
	plt.plot(sn.cycle, sn.measurement, '-.', color='gray', label=sn.name)
	
	# plot the chosen input series
	plt.plot(sn.cycle[c : c+lin], series_in, 'ko-', label='input series')
	
	# plot the expected & predicted outputs
	plt.plot(sn.cycle[c+lin : c+lin+lout], series_out, 'ks--', label='expected output series')
	plt.errorbar(sn.cycle[c+lin : c+lin+lout], predictions_mean, yerr=predictions_std, fmt='d--', ms=8, label='prediction')
	
	plt.plot(plt.xlim(), [attr.lower_limit, attr.lower_limit], 'r--')
	plt.plot(plt.xlim(), [attr.upper_limit, attr.upper_limit], 'r--')

	plt.xlabel('CycleCount', fontsize=15)
	plt.ylabel('Measurement AVG', fontsize=15)

	plt.title(attr.name)
	plt.legend(numpoints=1, loc='best')
	plt.tick_params(axis='both', labelsize=15)
	plt.grid(color='lightgray', linestyle='--')
	
	plt.savefig('output_example.png')

	plt.close()#show()
