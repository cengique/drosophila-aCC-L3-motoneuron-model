### Morphologically reconstructed model using the Neuron simulator

Prerequisites:

1. Download these files ([latest version](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/master.zip) 
or the [1.0 stable release](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/v1.0.zip))
1. Install [NEURON 7.1 or later](http://www.neuron.yale.edu/neuron/)

Run the simulation with:

- In Linux or Mac OS X, on the command line type ```nrngui exp-axon-tail2-chans-ext-axon-70um.ses``` 
- In Windows, right click on `exp-axon-tail2-chans-ext-axon-70um.ses` and open it with Neuron.

Once Neuron loads, click on `Init & Run` on the control window to run a sample simulation. The `IClamp` point process parameters can be adjusted to change input current injected to the soma.

 TUTORIAL
 ==========================
   An important part of this tutorial is the paper titled [Distal Spike Initiation Zone Estimation](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004189#pcbi-1004189-g0020), as the point of this tutorial will be to recreate a graph shown in this paper labeled Figure 2 Part A i. The lines of the graph represent the data output, when the researchers changed the current being injected into the model by the simulated IClamp. This data would become more important later in the overall experiment as they used it as a reference point in comparing different neuron models,
  
  Once the provided model is open there shall be several windows open on the computer, and althougth not mandatory,rearranging the windows is recommended for the sake of efficiency. At the very least the two graphs the RunControl window, and the 3D model window of the neuron should be visible; the other windows can be minimized.

![RunControl](Default-RunControl-Window.JPG)
![Model](Default-model.jpg)

![Graph 1](Default-Graph-1-window.JPG)
![Graph 2](Default-Graph-2-Window.JPG)

Now draw your attention to the window with the 3D model.

![Model](Default-model.jpg)

You should left-click with the mouse over the words _**SelectPointProcess**_. Unlike most programs now, in order to get the desired effect, the button must be held over the wrods rather than just clicked once. With this a small manu comes down, and while still holding the mouse's left button, the mouse should be moved over the words _**IClamp**_. The left button should then be released; when this is done, the window should change, and in the place of the 3D model should be a window with a column of variables and values.

![IClamp Window](IClamp-Parameters-Window.JPG)

These variables are the parameter of the Current clamp that is in the 3D model. If you return to the graph in the paper, you will notice a small table above the graph that has number values. These numbers represent
