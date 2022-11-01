# Morphologically reconstructed model using the NEURON simulator

## Prerequisites:

1. Download the latest [drosophila-aCC-L3-motoneuron-model](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/master.zip)
or the [1.0 stable release](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/v1.0.zip) and extract the ZIP file to a folder on your computer
1. Install [Python](https://www.python.org/downloads/) 
1. Install [NEURON 7.1 or later](http://www.neuron.yale.edu/neuron/)

## Testing

To check if NEURON is properly set up for use with Python:
 1. Open Anaconda Prompt or a terminal program (command prompt, bash, terminal)
 2. Type in `idle`, `ipython`, or `py` and press the Enter key
 3. Enter `from neuron import h`
 
If installed properly, the last line should not create any errors.

## Opening the simulation:

### Linux/MacOS
- In Linux or Mac OS X, navigate to the folder that holds the model ```drosophila-aCC-L3-motoneuron-model-master/neuron-model``` 
- To open the model, switch to a terminal and type ```nrngui "experiment.ses"``` for a SES file and ```python experiment.py``` for PY file.

### Windows
- In Windows, right click on the SES file and open it with NEURON
- If you do not see the option, select `Open with...` and navigate to `C:\nrn\bin\neuron`
- For PY files, open the command prompt (CMD) and type ```py experiment.py```

## Running the simulation
Once NEURON opens, look for `Init & Run` on the control window to run
a sample simulation. The `IClamp` point process parameters can be
adjusted to change input current injected to the soma. See under
Tutorials for more manipulations.

## Available experiment files

- `exp-axon-tail2-chans-ext-axon-70um.ses` - published base model that contains an extended axon containing Na-K spiking channels at 70um distance from its soma.
- `exp-axon-tail2-chans-ext-axon-70um-10x-mimic-sustained-random.py` - an extension of the base model that has 10 predefined synaptic locations to test sustained inputs to mimic spontaneous rhythmic current (SRC) responses.

## Tutorials

- [Replicate Paper Figures with NEURON](tutorial-replicate-paper-figure/README.md)
- [Python with NEURON](tutorial-python-neuron/README.md)
- [Saturating synapses with stimulus](tutorial-synaptic-saturation/README.md)
