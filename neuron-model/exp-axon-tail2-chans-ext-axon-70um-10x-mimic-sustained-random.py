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

aynrand_num = h.Random()
pc = h.ParallelContext()
aynrand_num.ACG(pc.time())
aynrand_num.normal(15,200)


aynrand_start = h.Random()
aynrand_start.ACG(pc.time())
aynrand_start.normal(200,1500)

synl = []
nsl = []
ncl = []

def set_syn_objs(*numsyn):
    """Create synapse, NetStim, and NetCon objects"""
    for i in numsyn:
        print(f"dendrite[{i}]\n")
        syn = h.ExpSyn(h.dendrite[i](0.5))
        ns = h.NetStim(h.dendrite[i](0.5))
        nc = h.NetCon(ns, syn)
        synl.append(syn)
        ncl.append(nc)
        nsl.append(ns)

def set_syn_pars(weight = .00018, tau = 5, interval = 10, magepsc = 20):
    """Set parameters of existing objects"""
    print(f"Setting: weight={weight}, tau={tau}, interval={interval}, magepsc={magepsc}")
    for nc in ncl:
        syn = nc.syn()
        ns = nc.pre()
        syn.tau = tau
        syn.e = 0
        ns.interval = interval
        ns.number = 3 + aynrand_num.repick()
        ns.start = 10 + aynrand_start.repick() #//+ (i-1)*interval/numsyn 
        ns.noise = 0
        nc.weight[0] = weight * magepsc


'''
 * synapses:
 * top dend: 685, 524, 520, 626
 * bot dend: 205, 357, 464, 588, 513, 48
'''

set_syn_objs(685, 524, 520, 626, 205, 357, 464, 588, 513, 48)
set_syn_pars()                  # use defaults

h.load_file('stdrun.hoc')
h.finitialize(-65 * mV)
h.continuerun(600 * ms)
