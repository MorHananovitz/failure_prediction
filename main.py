import numpy as np
from load_data import load
import plot

# ------------------------------- #
#        load training data       #
# ------------------------------- #

training_data = load('raw_weekend.csv')

# ------------------------------- #
#     visualize training data     #
# ------------------------------- #

# plot all data
#for d in training_data:
#	plot.data(d)

# plot specific part attribute data, e.g., "CDI - Distance"
#for d in training_data:
#	if d.name == 'CDI - Distance':
#		plot.data(d)

# ------------------------------- #
#              train              #
# ------------------------------- #

# Number Of Serial-Numbers
NOSN = len(training_data[0].serial_numbers) # [0] is technical - no meaning

lin = 10 # length of input time-series
lout = 8 # length of output time-series

# Cross validation is necessary because of very few data samples - currently only 10. Thus I'm implementing here leave-1-out.

attribute = []
models = []

for i in range(NOSN)[:-1]:
	
	# save 1 serial number for validation
	sn_valid_idx = i
	sn_train_idx = np.delete(np.arange(NOSN), sn_valid_idx)

	# train a model for part attribute "CDI - Upper Lip Radial Thickness"
	for d in training_data:
		if d.name == 'CDI - Upper Lip Radial Thickness':
			attr, m = d.train(lin, lout, sn_train_idx, sn_valid_idx, epochs=20)
			models.append(m)

# ------------------------------- #
#           predictions           #
# ------------------------------- #

# picking up some data as an example from validation data

c = 8 # cycle to start from
s = 10 # number of serial number. This is the last one, kept for test

#input_series = attr.data_to_validate[c : c+lin]
#expected_output_series = attr.data_to_validate[c+lin : c+lin+lout]
input_series = list(attr.serial_numbers[s-1].measurement[c : c+lin])
expected_output_series = list(attr.serial_numbers[s-1].measurement[c+lin : c+lin+lout])

# standardize
xs = attr.standardize(input_series, input_series)

# reshape data - necessary for NN input shape
xs = np.reshape(input_series, (1, lin, 1))

# actually predict something at last! (predict with all of the models)
ys = [models[j].predict(xs) for j in range(len(models))]

# bring prediction back to real world scale
y = []
for y_i in ys:
	y.append(attr.scaler.inverse_transform(y_i.reshape(1,-1)))

# mean and standard deviation of predictions
predictions_mean = np.mean(y, axis=0)
predictions_std = np.std(y, axis=0)

# now plot it
plot.manual(attr,
			input_series,
			expected_output_series,
			predictions_mean[0],
			predictions_std[0],
			lin, lout, c, s-1)






