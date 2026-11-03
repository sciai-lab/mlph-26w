Exercise Sheet 3 — simulated CT scan

The dataset describes a simulated scan of a 99 x 117 image at 30 angles,
with 155 parallel rays per angle.

Loading from a notebook or script in sheet03/:
    from ct_data import load_ct_data
    X, y = load_ct_data()

The helper generates data/design_matrix.npy on first use and reuses it on
later calls. Only NumPy is required. The large generated array is ignored
by Git.
You can also run python ct_data.py once to create the matrix, then load
data/design_matrix.npy and data/sino.npy directly.

ARRAYS AND ORDERING
X: (11583, 4650), float64, pixels x rays.
y: (4650,), float64, returned by the helper.
sino.npy is stored with shape (1, 4650); flatten it for fitting.

Image shape: (99, 117), flattened in NumPy C order (column index varies fastest).
Display an image with w.reshape(99, 117), origin='upper'.
Sinogram shape: (30, 155), ordered first by angle, then by detector offset.
Display y.reshape(30, 155), origin='lower', with angle as the first axis.
A column of X has the image layout; a row of X has the sinogram layout.

FORWARD MODEL
The numerical model is y = X.T @ w + measurement error. Do not fit an
additional intercept. X[k,j] is the exact path length of ray j through pixel k,
in units of the pixel width. Most entries are zero, because a ray crosses only
few pixels. Pixels are unit squares.

Pixel centers have coordinates x=-58,...,58 and y=-49,...,49, in unit steps.
The angle parameters are 6,12,...,180 degrees. A ray's direction is (cos(theta),-sin(theta)) and its origin is
offset*(sin(theta),cos(theta)). The 155 signed offsets run from -77 to
77 in unit steps, so neighbouring rays are one pixel width apart. Some rays
at the outermost offsets miss the image; their columns of X are zero.

The data contain measurement error; no noise standard deviation is specified.
Some values of y are slightly negative (I_1 > I_0) because of measurement
error; this is expected.
