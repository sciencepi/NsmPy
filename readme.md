# NsmPY

NsmPy is an open-source Numerical, Scientific and Mathematical library built and designed to make
calculating a breeze. At the time of this release, Alpha 1.0.1, there is only one type of data
structure, "matrix"

# What is a "matrix"?
The matrix data type is heavily based off of another incredible library, NumPy. It is similar
in that all "matrixes" contain two elements - the main "data" part, known as the `as_array`
component in the code. This is responsible for holding information about the matrix - its
elements. The other thing the  two datatypes have in common is the use of `shape`. This is
a feature also found in an `np.array()` structure. The shape, unlike in the NumPy array,
is actually used to define the dimensions of the matrix. So, for example, if you were to
define the matrix:
```Python
 x = matrix([0, 0, 0, 0], shape=(2,2))
```
You would create a matrix with dimensions 2x2 and with elements 0, 0, 0 and 0. This is
incredibly useful in most python scripts that utilise this property - you don't need to do
any _special_ formatting on the structure - a raw list will do just fine. This is also helpful
when you compare it to NumPy's array system - just look:
```Python
# NumPy version.
x = np.array([[0,0],
              [0,0]])
# NsmPy version.
x = matrix([0,0,0,0], (2,2))
```
Not only is the NsmPy version much more elegant, it is more efficient as well.
### What else can you do with a matrix?
Matrixes are actually very versatile. They actually behave similar to python lists, and
can be indexed, and can also have their elements changed. Not only that, but you can
actually create more matricies from one matrix, and you can even generate identity
matricies.

Here is a simple program which does some matrix multiplication:
```Python
from nsmpy import matrix # get the matrix datastructure.
x = matrix([2,4,1,6], shape=(2,2)) # create a matrix with dimensions 2x2.
y = matrix([1,5,6,7], shape=(2,2))
# in order to do matrix multiplication (dot), both matricies must be
# the same in element-size, and must have the general matrix-multiplication
# rule in place.
z = x.matrix_mult(y) # matrix_mult(y) -> matrix()
print (z)
```
The output of this program is:
```python
 26  38  37  47 
 # or:
 matrix([26, 38, 37, 47])
```
### Installation
NsmPy requires `NumPy version 16.0.0` or greater, and literally nothing else.
I strongly reccomend you use `NumPy 16.0.1` since the latest version spews out alot  of
nasty looking warnings.

You can install the module as well as NumPy using the following:
```sh
linux/mac:
user:$ sudo pip uninstall numpy
user:$ sudo pip install numpy==16.0.1
user:$ sudo pip install nsmpy

Windows (x64/x86):
C:\> pip uninstall numpy
C:\> pip install numpy==16.0.1
C:\> pip install nsmpy
```
And you're done!
### This is open source!
You can modify the code to your hearts content! There are no limits on distributing your own
custom version of the code, but beware - you must not distribute your custom version under the
name of the actual release of the code - this could confuse people as to why certain things arent
working like the readme said they would - so please don't do that.

Kind regards, SciencePi

NsmPy (C) 2020 SciencePi