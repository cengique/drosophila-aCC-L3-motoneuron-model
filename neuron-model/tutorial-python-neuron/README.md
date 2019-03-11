# How to setup Python with the NEURON Module
You should have [NEURON](https://www.neuron.yale.edu/neuron/download) installed before proceeding.

First install the latest version of Python (3.7 as of 2019) for your system. Installing through [Anaconda](https://www.anaconda.com/distribution/) is recommended.

### Windows
1. Make sure pip has been installed and the correct environment path variables have been set up.
2. Open the Anaconda Prompt application and enter: `pip install pyneuron`

If you encounter any issues, the last known working version of [Python 2.7 32 bit](https://www.python.org/download/releases/2.7/).
### Linux
1. Make sure Python and pip are already installed.
2. To begin entering Python input in the Terminal, enter `nrngui -python`
 ### Testing
 To check if NEURON is properly set up for use with Python:
 1. Open Anaconda Prompt
 2. Type in `idle` and press the Enter key
 3. Enter `from neuron import h`
 
 If installed properly, the last line should not create any errors.
 ## Tutorials

 [Recording Cell Compartment Voltage Values](../tutorial-python-neuron/RecordingCellCompartmentVoltageValues.md)
