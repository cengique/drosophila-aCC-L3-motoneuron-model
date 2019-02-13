### Morphologically reconstructed model using the NEURON simulator

#### Prerequisites:

1. Download the latest [drosophila-aCC-L3-motoneuron-model](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/master.zip)
or the [1.0 stable release](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/v1.0.zip)
1. Install [NEURON 7.1 or later](http://www.neuron.yale.edu/neuron/)

### Opening the simulation:

#### Linux/MacOS
- In Linux or Mac OS X, navigate to the folder that holds the model ```drosophila-aCC-L3-motoneuron-model-master/neuron-model``` 
- In the terminal type ```nrngui exp-axon-tail2-chans-ext-axon-70um.ses``` to open the model

#### Windows
- In Windows, right click on `exp-axon-tail2-chans-ext-axon-70um.ses` and open it with NEURON or
- If you do not see the option, select `Open with...` and navigate to `C:\nrn\bin\neuron`

### Running the simulation
Once NEURON opens, look for `Init & Run` on the control window to run a sample simulation. The `IClamp` point process parameters can be adjusted to change input current injected to the soma. See under Tutorials for more information.

 #### Tutorials

- [Replicate Paper Figures with NEURON](tutorial-replicate-paper-figure/README.md)
- [Python with Neuron](tutorial-python-neuron/README.md)
