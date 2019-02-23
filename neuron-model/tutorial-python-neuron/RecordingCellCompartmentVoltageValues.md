# Recording Cell Compartment Voltage Values

This tutorial will cover using the NEURON module with Python. See [How to setup Python with the NEURON Module](README.md) for getting setup if you have not already. If you need further information than this tutorial will deliver, check Yale's full documentation of [NEURON + Python](https://www.neuron.yale.edu/neuron/static/docs/neuronpython/index.html)

### Prerequisities
* [drosophila-aCC-L3-motoneuron-model](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/master.zip) or the [1.0 stable release](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/v1.0.zip)
* [Anaconda](https://www.anaconda.com/distribution/) or Python and its included packages
* [NEURON 7.1 or later](http://www.neuron.yale.edu/neuron/)

The following lines of code may be entered sequentially in the Python shell or all at once through a `.py` script. The script is already inside the motoneuron model at `drosophila-aCC-L3-motoneuron-model-master/drosophila-aCC-L3-motoneuron-model-master/neuron-model/python_hoc.py`

## Launching IDLE (Python Shell)
IDLE will be the designated environment for inputting Python code. Anaconda and the default installations of Python should already include the program. Be sure to hit the Enter key when you are ready to execute a line.

1. Open Anaconda Prompt
2. Change Directory to the folder containing our NEURON model using `cd`
    * Example for Windows, note what may need to be edited:
    ```
    cd C:/Users/CHANGE_TO_YOUR_USERNAME/Downloads/drosophila-aCC-L3-motoneuron-model-master/drosophila-aCC-L3-motoneuron-model-master/neuron-model
    ```
3. Enter `idle` to start the Python shell
4. Switch to the new window to continue with below

## Running Python Code
### Running an Entire Script
This option is for experienced programmers. The `python_hoc.py` file will contain brief explanations of what each line of code does. Refer to the next section for a more in-depth explanation. To run the file, do the following:
1. In the Python shell, select File > Open...
2. Choose the file `python_hoc.py`
3. In the new window, run the script with Run > Run Module `F5`

To make a script, select File > New File. In the new window, enter the desired code to run. Once completed, save the `.py` file. The directory of the model is recommended since it contains the files necessary for using the features of the model. The file is run the same way as explained above.

### Running Code Line-by-Line (recommended for new users)
This section will detail running a NEURON simulation to record the voltage values from the cell compartments.

In order to use the Neuron module, we will need to import a HocObject `h`. Including `gui` will open NEURON's interface (gui) to allow for viewing the simulation.

```python
from neuron import h, gui #gui is optional 
```

The `h` module allows python to interface with hoc. Code will be passed to `h` in the form of strings as shown in the next instruction. [See using the h variable for more information.](https://www.neuron.yale.edu/neuron/static/py_doc/programming/python.html#python-accessing-hoc)

After importing the HocObject, use the following lines of code to import the needed files for the simulation:

```python
h('load_file("inc-first.ses")')  #load ion channels
h('{load_file("neuron-CB-ext-axon-2pieces-chans-ext-axon-70um.ses")}')  #load cellbuilder
h('load_file("fitfuncs.hoc")')  #load common functions
h('load_file("stats.hoc")')
```

The simulation has to run for a certain duration. This tutorial will use 600 milliseconds. Duration can be set in the `h` variables through `tstop`:

```python
h.tstop = 600
```

Voltage values will be recorded in a hoc vector. To declare a vector and specify what it will record during the simulation, use:


```python
h('objref vec') #declares a vector
h('vec = new Vector()') #initializes the vector
h('vec.record(&soma[0].v(.5))') #sets the vector for receiving simulation data
```

Use the following to set the graph in NEURON to display the simulation data. A new window in NEURON should appear once the graph has been initialized. Note how the axes change when set the presets.

```python
h('objref g') #declares a graph
h('g = new Graph()') #initializes the graph
h('g.size(0,10,-1,1)') #sets presets for axes of the graph
```

Now that everything is set up properly, run the simulation with:

```python
h.finitialize()  #Must be called before run().
h.run()  #Runs simulation.
h('vec.plot(g, .1)') #plots the data on the graph
```

Once the simulation ends, the data can be saved for later in a `.dat` file. Future tutorials will use MATLAB or tools from Anaconda for viewing the data. The following lines will save the recorded data in a binary file called `voltage_recording.dat`.

```python
h('strdef my_file') #declares a file
h('my_file = "voltage_recording.dat"') #sets voltage_recording as the target
h('objref save')
h('save = new File(my_file)')
h.save.wopen()
n = h.vec.vwrite(h.save) #sets n to 1 if the save was successful, 0 if not
if n == 1:
    h.save.close()
```
# _________________________________________________________________
## Viewing Voltage Values in Matlab with Pandora ToolBox
 
 First, you will need the [Pandora ToolBox](https://github.com/cengique/pandora-matlab)
 
Copy the `voltage_recording.dat` to the current MATLAB directory. Next, to load the `voltage_recording.dat` file in MATLAB, type in the following command in the MATLAB prompt:

`a_trace = trace('voltage_recording.dat', 25e-6, 1e-3,'my_trace',struct('file_type','neuron')); plot(a_trace)`
 

![Voltage Plot](voltage_trace_plot.png)


