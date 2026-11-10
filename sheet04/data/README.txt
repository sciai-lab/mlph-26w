Exercise Sheet 4 — data

gravityspy_glitches.csv
    6866 glitches recorded by the two LIGO detectors during the first
    observing run, between September 2015 and January 2016, each with its
    Gravity Spy class label, based on its time-frequency image. One row per
    glitch, with a header row.

COLUMNS
gravityspy_id   unique identifier of the glitch
event_time      time of the glitch, GPS seconds (seconds since 6 January 1980)
ifo             detector: H1 (Hanford) or L1 (Livingston)
duration        duration of the trigger [s]
peak_frequency  frequency of the loudest part of the trigger [Hz]
central_freq    central frequency of the trigger [Hz]
bandwidth       frequency bandwidth of the trigger [Hz]
amplitude       amplitude of the trigger in strain units (order 1e-22)
snr             signal-to-noise ratio of the trigger
label           glitch class, one of 18 (Blip, Koi_Fish, Scattered_Light, ...)
sample_type     train, validation or test: the random split used for the
                original Gravity Spy classifier (Bahaadini et al. 2018);
                not needed for this exercise

The six numerical trigger parameters come from the Omicron pipeline, which
searches the detector output for excess power in the time-frequency plane.

SOURCE
S. Coughlin, Gravity Spy Training Set, Zenodo (2018),
https://doi.org/10.5281/zenodo.1486046, licensed CC BY 4.0
(file trainingset_v1d1_metadata.csv). We kept the glitches of the first
observing run and the columns above; image links and constant or internal
columns were dropped. We also removed the single example of the class
1080Lines and the classes Helix, Violin_Mode and 1400Ripples, which occur
almost only on a single day.
Values are unchanged.

Gravity Spy: M. Zevin et al., Class. Quantum Grav. 34, 064003 (2017).
Dataset and classifier: S. Bahaadini et al., Information Sciences 444,
172-186 (2018).
