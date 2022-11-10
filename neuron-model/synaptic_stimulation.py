import numpy as np
from neuron.units import ms, mV
from matplotlib import pyplot
from bokeh.io import output_notebook
import bokeh.plotting as plt
from bokeh.models.ranges import DataRange1d
from bokeh.models.tools import CrosshairTool, ExamineTool
import numpy as np
from bokeh.io import export_svg

# Dictionary for netcon objects indexed by section number that hold the synapse and netstim objects
syns = {}

class Synapse():
    
    def __init__(self, name, sec, syn, ns, nc):
        self.name = name
        self.sec = sec
        self.syn = syn
        self.ns = ns
        self.nc = nc
        
    def set_stim(self, ps, weight = .00018, tau = 5, interval = 10, magepsc = 20, syne = 0, number = 1, start = 10):
        """Set parameters of specified synapse"""
        nc = self.nc
        syn = self.syn
        ns = self.ns
        print(f"Setting: weight={weight}, tau={tau}, interval={interval}, magepsc={magepsc}, syne={syne}, number={number}, start={start}")
        syn.tau = tau
        syn.e = syne
        ns.interval = interval
        ns.number = number
        ns.start = start
        ns.noise = 0
        nc.weight[0] = weight * magepsc
        ps.color(2, self.sec(0.5))
        
    def __str__(self):
        return print(f"Synapse {self.name}: weight*magepsc={self.nc.weight[0]}, tau={self.syn.tau}, interval={self.ns.interval}, syne={self.syn.e}, number={self.ns.number}, start={self.ns.start}")

def create_syns(h, *secs):
    """Factory method to create synapse, NetStim, and NetCon objects"""
    for sec in secs:
        print(f"Creating synapse on {sec}")
        syn = h.ExpSyn(sec(0.5))
        ns = h.NetStim(sec(0.5))
        nc = h.NetCon(ns, syn)
        nc.delay = 0
        syn_obj = Synapse(str(sec), sec, syn, ns, nc)
        syns[str(sec)] = syn_obj

def extract_mini_metrics(h, vc_current, start_time_ms):
    ampi = np.argmin(vc_current)
    risetime_ms = ampi*h.dt - start_time_ms
    amp_nA = vc_current[ampi] - vc_current[0]
    falltime_i = np.where(vc_current[ampi:] > (vc_current[round(start_time_ms/h.dt)] - 0.000001))
    if np.shape(falltime_i)[1]> 0:
        falltime_ms = falltime_i[0][0]*h.dt
    else:
        falltime_ms = np.shape(vc_current)[0]*h.dt - start_time_ms - risetime_ms
    return {"risetime_ms": risetime_ms, "falltime_ms": falltime_ms, "amp_nA": amp_nA}

def run_amp_sweep(h, ps, vc_current, syn, min_amp, max_amp, steps):
    step_num = 0    
    for amp in np.logspace(np.log10(min_amp), np.log10(max_amp), steps):
        print(f"Simulating step of synaptic weight of {amp}.")
        h.restoreState()
        syn.set_stim(ps = ps, weight = amp, tau=5, interval = 0, number = 1, magepsc = 1)
        h.finitialize()
        h.continuerun(60 * ms)
        if not step_num:
            vc_currents = np.empty((vc_current.size(), steps))
            vc_currents[:,0] = np.array(vc_current)
        else:
            vc_currents[:, step_num] = np.array(vc_current)
        step_num += 1
    return vc_currents

def plot_amp_sweep(t, vc_currents):
    f = plt.figure(x_axis_label="t (ms)", y_axis_label="VC current (pA)", frame_width = 800)
    f.add_tools(CrosshairTool())
    for step in np.arange(np.shape(vc_currents)[1]):
        f.line(np.array(t), vc_currents[:,step] * 1e3, line_width=2)
    f.x_range = DataRange1d(start = 9, end = 50)
    f.y_range = DataRange1d(start = -70, end = 0)
    plt.show(f)

