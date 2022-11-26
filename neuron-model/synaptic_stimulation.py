import numpy as np
from neuron.units import ms, mV
from matplotlib import pyplot
from bokeh.io import output_notebook
import bokeh.plotting as plt
from bokeh.models.ranges import DataRange1d
from bokeh.models.tools import CrosshairTool, ExamineTool
from bokeh.io import export_svg
import numpy as np
import pandas as pd

# Dictionary for netcon objects indexed by section number that hold the synapse and netstim objects
syns = {}

class Synapse():
    
    def __init__(self, name, sec, syn, ns, nc):
        self.name = name
        self.sec = sec
        self.syn = syn
        self.ns = ns
        self.nc = nc
        
    def set_stim(self, ps, weight = .00018, taurise = 1, taufall = 5, interval = 10, magepsc = 20, syne = 0, number = 1, start = 10):
        """Set parameters of specified synapse"""
        nc = self.nc
        syn = self.syn
        ns = self.ns
        print(f"Setting: weight={weight}, taurise = {taurise}, taufall={taufall}, interval={interval}, magepsc={magepsc}, syne={syne}, number={number}, start={start}")
        syn.tau1 = taurise
        syn.tau2 = taufall
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
        syn = h.Exp2Syn(sec(0.5))
        ns = h.NetStim(sec(0.5))
        nc = h.NetCon(ns, syn)
        nc.delay = 0
        syn_obj = Synapse(str(sec), sec, syn, ns, nc)
        syns[str(sec)] = syn_obj

def extract_mini_metrics(h, vc_current, start_time_ms):
    start_dt = round(start_time_ms/h.dt)
    ampi = np.argmin(vc_current[start_dt:])
    risetime_ms = ampi*h.dt
    baseline_nA = vc_current[start_dt]
    #print(f"baseline_nA: {baseline_nA}, argmin: {ampi}, min: {vc_current[ampi]}")
    max_i = start_dt + ampi
    amp_nA = vc_current[max_i] - baseline_nA
    falltime_i = np.where(vc_current[max_i:] > (baseline_nA - 0.00001))
    if np.shape(falltime_i)[1]> 0:
        falltime_ms = falltime_i[0][0]*h.dt
    else:
        falltime_ms = np.shape(vc_current)[0]*h.dt - start_time_ms - risetime_ms
    return {"risetime_ms": risetime_ms, "falltime_ms": falltime_ms, "amp_pA": amp_nA*1e3}

def run_amp_sweep(h, ps, vc_current, syn, min_amp, max_amp, steps):
    step_num = 0
    steps_list = np.logspace(np.log10(min_amp), np.log10(max_amp), steps)
    for amp in steps_list:
        print(f"Simulating step of synaptic weight of {amp}.")
        h.restoreState()
        syn.set_stim(ps = ps, weight=amp, taurise=1, taufall=5, interval=0, number=1, magepsc=1)
        h.finitialize()
        h.continuerun(60 * ms)
        if not step_num:
            vc_currents = np.empty((vc_current.size(), steps))
            vc_currents[:,0] = np.array(vc_current)
        else:
            vc_currents[:, step_num] = np.array(vc_current)
        step_num += 1
    return vc_currents, steps_list

def run_sweep_func(h, ps, vc_current, func, steps_list):
    step_num = 0
    for amp in steps_list:
        h.restoreState()
        func(amp)
        h.finitialize()
        h.continuerun(60 * ms)
        if not step_num:
            vc_currents = np.empty((vc_current.size(), len(steps_list)))
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
    return f

def get_sweep_metrics(h, vc_currents, steps_list):
    num_steps = np.shape(vc_currents)[1]
    for step in np.arange(num_steps):
        metrics = extract_mini_metrics(h, vc_currents[:,step], 10)
        if not step:
            metrics_df = pd.DataFrame(data=np.empty((num_steps, len(metrics))), columns=metrics.keys(), index=steps_list)
            metrics_df.iloc[step, :] = pd.Series(metrics)
        else:
            metrics_df.iloc[step, :] = pd.Series(metrics)
    return metrics_df

def plot_scatter_risetime_amp(minis_df):
    f = plt.figure(x_axis_label="rise time (ms)", y_axis_label="amplitude (pA)", frame_width = 400)
    f.add_tools(CrosshairTool())
    f.scatter(x='risetime_ms', y='amp_pA',  source=minis_df, alpha=0.3)
    #f.x_range = DataRange1d(start = 0.8, end = 1.1)
    #f.y_range = DataRange1d(start = -70, end = 0)
    plt.show(f)
    return f


def set_g_pas_dend(h, new_g_pas):
    sl = h.SectionList()
    sl.wholetree(h.soma[0])     # Add everything
    # Except electrode and extended axon section with Na-K channels
    sl.remove(h.electrode)
    sl.remove(h.axon_ext[1])
    for sec in sl:
        sec.g_pas = new_g_pas
