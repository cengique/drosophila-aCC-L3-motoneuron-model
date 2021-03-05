from neuron import h, gui
from neuron.units import ms, mV
# Experiment with 2-component axon extention tail, and Na-K channels
# in all compartments

# nrngui stuff and ion chans

h('load_file("inc-first.ses")')

# strdef file_name, ses_file, cb_file_name
file_name = "ext-axon-70um-10x-mimic-sustained-random"

cb_file_name = "ext-axon-70um-10x-mimic-sustained"

ses_file  = "neuron-CB-ext-axon-2pieces-chans-" + cb_file_name + ".ses"

# load CellBuilder
h('load_file("' + ses_file + '")')


# load common funcs
h('load_file("fitfuncs.hoc")')

#h('print_elec_cell()') #fix this 

# calc morph stats
h('load_file("stats.hoc")')

h('load_file("v-graph-bigger-axon-2pieces.ses")')

# enable or disable VC
h('load_file("vclamp_soma_-60mV.ses")')

# save state in this file
state_file_name = "state-neuron-CB+act+elec+ext-axon-2piece-chans-" + file_name + ".bin"

# load state first because it overrides parameters
state_w_syn = "state-neuron-CB+act+elec+ext-axon-2piece-chans-" + file_name + "-synapse-saved.bin"

h.restoreStateFromFile(state_w_syn)

# small adjustments

# increase VC duration
h.VClamp[0].dur[0] = 1000

# use ExpSyn object
magepsc = 20
interval = 10

aynrand_num = h.Random()
pc = h.ParallelContext()
aynrand_num.ACG(pc.time())
aynrand_num.normal(15,200)


aynrand_start = h.Random()
aynrand_start.ACG(pc.time())
aynrand_start.normal(200,1500)

def set_syn(*numsyn):
    count = 0
    syn = []
    ns = []
    nc = []
    
    for i in numsyn:
        print(f"dendrite[{i}]\n")
        syn.append(h.ExpSyn(h.dendrite[i](0.5)))
        nc.append(h.NetStim(h.dendrite[i](.5)))
        ns.append(h.NetCon(nc[count], syn[count]))
        syn[count].tau = 5
        syn[count].e = 0
        nc[count].interval = interval
        nc[count].number = 3 + aynrand_num.repick()
        nc[count].start = 10 + aynrand_start.repick() #//+ (i-1)*interval/numsyn 
        nc[count].noise = 0
        ns[count].weight[0] = .00018 * magepsc
        count += 1
      
'''
 * synapses:
 * top dend: 685, 524, 520, 626
 * bot dend: 205, 357, 464, 588, 513, 48
'''

set_syn(685, 524, 520, 626, 205, 357, 464, 588, 513, 48)
h.load_file('stdrun.hoc')
h.finitialize(-65 * mV)
h.continuerun(600 * ms)
