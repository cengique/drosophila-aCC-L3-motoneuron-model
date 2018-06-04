# Recording Cell Compartment Voltage Values



We wil be using the neuron module with python. See [here](README.md) for getting setup. Continuing further with the tutorial assumes that you have already installed: Python, Anaconda, & NEURON.

The following tutorial can either be completed entering one line of code at a time, or by typing in ALL of the following commands into a Python script and have them all run at once. Either way, the Python shell must be launched. 

## Launching IDLE (Python Shell)

To use  IDLE, first launch the Anaconda prompt. Once a black command window appears, type 'idle' followed by the ENTER key. This should launch IDLE. If you wish to make an entire script of the commands below, click FILE, then NEW FILE to open a blank Python file to write the commands in.  

## Running Scripts (all commands at once)
If you chose this option, it is important to note that when you are ready to run the code you have, to click the RUN tab, followed by Run Module(f5).


Next, we are going to be running a neuron simulation that will be recording voltage values from the cell compartments. 

In order to use the Neuron module, we will need to import a HocObject (h) and also have the option of also importing NEURONS interface (gui) by using the following line:

```
from neuron import h, gui #gui is optional 
```
The `h` variable allows python to interface with hoc. ([Using the h variable](https://www.neuron.yale.edu/neuron/static/py_doc/programming/python.html#python-accessing-hoc) )




After importing our HocObject we then need to load important files in hoc using the following lines of code:

```python
h('load_file("inc-first.ses")')  #load ion channels
h('{load_file("neuron-CB-ext-axon-2pieces-chans-ext-axon-70um.ses")}')  #load cellbuilder
h('load_file("fitfuncs.hoc")')  #load common functions
h('load_file("stats.hoc")')
```

Our simulation has to run for a certain duration, so let's set that duration to 600 milliseconds. We will be setting this duration in the `h` variables `tstop` attribute. simply call:

`h.tstop = 600`

We will be recording the voltage values in a hoc vector, so let's declare our vector and tell it what to record during the simulation.


```python
h('objref vec')
h('vec = new Vector()')
h('vec.record(&soma[0].v(.5))')
```

Now that the preliminary steps have been taken, we can now run our simulation with the following lines:



```python
h.finitialize()  #Must be called before run().
h.run()  #Run simulation.
h('vec.plot(g, .1)') #this will show the graph in NEURON
```
Once our simulation ends we can view our values in a software such as Matlab. But first, we have to write our data to a data file called `voltage_recording.dat` In order to do that, type the following lines:

```python
h('strdef my_file')
h('my_file = "voltage_recording.dat"')
h('objref save')
h('save = new File(my_file)')
h.save.wopen()
n = h.vec.vwrite(h.save)
if n ==1:
    h.save.close()
```
 
    
    
 ## Viewing Voltage Values in Matlab with Pandora ToolBox
 
 First, you will need the [Pandora ToolBox](https://github.com/cengique/pandora-matlab)
 
Place the `voltage_recording.dat` in the current MATLAB directory. Next, to load the `voltage_recording.dat` file in MATLAB, type in the following command in the MATLAB prompt:

`a_trace = trace('voltage_recording.dat', 25e-6, 1e-3,'my_trace',struct('file_type','neuron')); plot(a_trace)`
 

![Voltage Plot](voltage_trace_plot.png)



