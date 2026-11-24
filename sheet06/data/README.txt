HIGGS event classification data for Exercise Sheet 06

The three compressed NumPy archives contain 500,000 simulated events.
Use numpy.load to open each file. The x array contains 28 float32 input
features per event. The y array contains the labels, with 1 for signal
and 0 for background. The rows array gives the original zero-based row
indices for provenance. Use x and y for modelling.

  File             Events
  train.npz       400,000
  validation.npz   50,000
  test.npz         50,000

The test sample comes from the original dataset's test partition. The
first 21 input columns contain simulated detector observables such as
jet momenta. The remaining seven contain derived quantities such as
reconstructed invariant masses. The feature order follows the archive.

The exercise files are fixed subsets of the HIGGS HDF5 release, with
duplicate feature vectors removed before sampling. Credit goes to
Daniel Whiteson, HIGGS (2014), UCI Machine Learning Repository,
licensed under CC BY 4.0.
https://doi.org/10.24432/C5V312
https://mlphysics.ics.uci.edu/data/higgs/

Physics benchmark by Pierre Baldi, Peter Sadowski and Daniel Whiteson.
https://arxiv.org/abs/1402.4735
