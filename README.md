# Drosophila 3rd instar larval aCC motoneuron

This the the modeling package to accompany paper:

Cengiz Günay, Fred Sieling, Logesh Dharmar, Wei-Hsiang Lin, Verena
Wolfram, Richard Marley, Richard A. Baines, and Astrid A. Prinz. 
Estimation of spike initiation zone and synaptic input parameters of
an identified larval Drosophila motoneuron using a morphologically
reconstructedor electrical model.
*In preparation*.

Download from:
http://www.biology.emory.edu/research/Prinz/Cengiz/Gunay_etal_2014.zip

## Requirements:

XPPAUT 5.99 - http://www.math.pitt.edu/~bard/xpp/xpp.html

Neuron 7.1 - http://www.neuron.yale.edu/neuron/

PANDORA 1.3b - http://software.incf.org/software/pandora

## Directories:

**xpp-models/**	Isopotential and ball-and-stick models and their figures (see figure_models.m).

**neuron-model/** Multicompartmental model in Neuron (see figures.m).

## Workflow/history of project:
- Channel data were fit with the Neurofit tool and then re-adjusted with param-fitter in Matlab.
- XPP models were built with these channels and hand-tuned to fit observed f-I, v-I, and delay.
- Neuron model used these channels and some properties of the ball-and-stick model.
- Morphological reconstruction passive parameters were tuned to recorded capacitance responses.
- Channel distribution hand tuned to mimick observed current responses.

Please report problems/suggestions/comments to:
Cengiz Gunay <cengique AT users.sf.net>
2014/01/08