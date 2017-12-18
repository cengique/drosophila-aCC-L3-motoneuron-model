from neuron import h



#load ion channels
h('load_file("inc-first.ses")')

#load cellbuilder
h('{load_file("neuron-CB-ext-axon-2pieces-chans-ext-axon-70um.ses")}')

#load common funcs
h('load_file("fitfuncs.hoc")')
h('load_file("stats.hoc")')

h.tstop = 600

#records voltage of cell compartment in a vector
h('objref vec')
h('vec = new Vector()')
h('vec.record(&soma[0].v(.5))')

#must call before run
h.finitialize()

#run simulation
h.run()

#writes vector to file which can be processed in matlab via Pandoras 'trace' function
h('strdef my_file')
h('my_file = "voltage_recording.txt"')
h('objref save')
h('save = new File(my_file)')
h.save.wopen()
n = h.vec.vwrite(h.save)
if n ==1:
    h.save.close()


#in matlab with the 'voltage_recording.txt' file the right directory, call the following line:
    #a_trace = trace('voltage_recording.txt', 25e-6, 1e-3,'my_trace',struct('file_type','neuron')); plot(a_trace)


