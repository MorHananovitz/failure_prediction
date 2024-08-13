# Failure Prediction Model 
by Eyal Oren and Mor Hananovitz

## Project's goal
To develop a program able to predict when a given physical part (i.e. has its own serial number) will fail quality control tests. The program accomplishes that by generating a forecast of various features into the future, where each feature is allowed to experience changes within given limits. Failure is declared at the moment one of the features exceeds one of its spec limits.

## ------------

## Introduction 
In this work we will demonstrate failure prediction model based on previously collected data.
As technology evolves, processes improve, but not everything is changing. We shall take information collected on parts used since 2013 and implement on the same parts used today.

<img src=part.JPG align="center" width=700>
Fig. 1: Part in Question

  - Inputs: Time series (i.e CycleCounts) of the average measured value

<img src=trend_example.png align=“center” width=700>
Fig. 2: Trend Example
  - Features: Parameters collected based on part's manufacture specs
  - Output: Behavioral prediction in the form of a graph to demonstrate next steps of the part
  - Validation: Using a part with long cycle count for validation

<img src=output_example.png align=“center” width=700>
Fig. 3: Output Example of test sample

## How Does the Data Looks Like?

Our data is composed out of 10 parts (Same Make and Model - different Serial Numbers) that ran through the machine in a long period of time (i.e CycleCount, around 30-40 for each part).

Each part has 10 features (i.e measured parameters) that define the part's performance in the machine.
Nine parts (Serial Numbers 1-9) were used for training with leave-1-out cross-validation. The last part was left for testing. 

## Model
LSTM based, multi-step prediction, currently fixed lengths for input array and for output array. As per the cross-validation, there are 9 models trained, and inference is the mean of this ensemble.

## Dependencies
	* numpy
	* pandas
	* matplotlib
	* scikit-learn
	* keras 2.x.x
	* tensorflow 1.x.x

## Program's Workflow
Load data -> visualize data (optional) -> train -> make predictions -> visualize predictions

In the current setup the program trains on one feature at a time - the feature in this case is "CDI - Upper Lip Radial Thickness" - found in _main.py_ under the training data (line 47). Currently to move between features it must be done manually (full list of features by name is given below).

Notice that currently the concept "feature" is also named in different places by property / parameter / part attribute.

In order to run the model as is - clone the Git repository and run _main.py_ file.

If you want to view all of the parts (serial numbers) used for training by features one after the other - identical to figure 1 go to _main.py_ in the _visualize training data_ section - and uncomment lines 20-22.

## Features (i.e measured parameters)
Must be copied as is!

	CDI - Flatness
	CDI - Diameter (Inner)- Post Strip
	CDI - Upper Lip Radial Thickness
	CDI - Avg Wall Cell Thickness
	CDI - Miscellaneous- Distance
	Surface Roughness- Post Blast
	Inner Honey Comb Ra (L1 - L6)
	UV Inspection 1=Pass, 0=Fail
	Particle Values ( <1.0 p/cm2 at 0.3um)
