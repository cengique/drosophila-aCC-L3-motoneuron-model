### Drosophila 3rd instar larval aCC motoneuron

**Note:** For previous versions of the models and information about changes, see [Releases](https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/releases)

This is the modeling package to accompany the paper:

Cengiz Günay, Fred Sieling, Logesh Dharmar, Wei-Hsiang Lin, Verena Wolfram, Richard Marley, Richard A. Baines, and Astrid A. Prinz. **Distal Spike Initiation Zone Location Estimation by Morphological Simulation of Ionic Current Filtering Demonstrated in a Novel Model of an Identified Drosophila Motoneuron**,
[PLoS Comput Biol 2015, 11(5): e1004189](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004189)

OpenSourceBrain page:
http://www.opensourcebrain.org/projects/drosophila-acc-l3-motoneuron-gunay-et-al-2014

ModelDB accession number is: 152028
https://senselab.med.yale.edu/modeldb/ShowModel.asp?model=152028

Download from:

https://github.com/cengique/drosophila-aCC-L3-motoneuron-model/archive/master.zip
OR
http://www.biology.emory.edu/research/Prinz/Cengiz/Gunay_etal_2014.zip

Single compartmental, ball-and-stick models implemented in XPP and full morphological model in Neuron. Paper correlates anatomical properties with electrophysiological recordings from these hard-to-access neurons. For instance we make predictions about location of the spike initiation zone, channel distributions, and synaptic input parameters.

## Requirements:

XPPAUT 5.99 - http://www.math.pitt.edu/~bard/xpp/xpp.html

Neuron 7.1 - http://www.neuron.yale.edu/neuron/

jNeuroML - https://github.com/NeuroML/jNeuroML

## Directories:

**xpp-models/**	Isopotential and ball-and-stick models.

**neuron-model/** Multicompartmental model in Neuron. Use exp-axon-tail2-chans-ext-axon-70um.ses as the main file.

**NeuroML2/** (*Under Construction*) Ports of all models to NeuroML2 and LEMS. Includes [OMV tests](https://github.com/OpenSourceBrain/osb-model-validation) to check for consistency with the original models: [![Build Status](https://travis-ci.org/cengique/drosophila-aCC-L3-motoneuron-model.svg)](https://travis-ci.org/cengique/drosophila-aCC-L3-motoneuron-model)

## Workflow/history of project:
- Channel data were fit with the Neurofit tool and then re-adjusted with param-fitter in Matlab.
- XPP models were built with these channels and hand-tuned to fit observed f-I, v-I, and delay.
- Neuron model used these channels and some properties of the ball-and-stick model.
- Morphological reconstruction passive parameters were tuned to recorded capacitance responses.
- Channel distribution hand tuned to mimick observed current responses.

Please report problems/suggestions/comments to: 

Cengiz Gunay (cengique AT users.sf.net)
