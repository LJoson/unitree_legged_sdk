# unitree_legged_sdk
python wrapper of unitree_legged_sdk with [pybind11](https://github.com/pybind/pybind11), only support python3.x now.


Install from pip
==================

unitree_legged_sdk is available as wheel packages for Linux distributions, you can install with pip:

```
python -m pip install -U pip
python -m pip install -U unitree_legged_sdk
```

# Build from source

If you want to build unitree_legged_sdk with some options not as default, or just like to build everything yourself, it is not difficult to build unitree_legged_sdk from source.

## Prerequisites

**On Unix (Linux, OS X)**

* A compiler with C++11 support
* CMake >= 3.4


## Build
1. clone unitree_legged_sdk and init submodule.
```bash
cd /pathto/unitree_legged_sdk
git submodule init && git submodule update
```
2. build.
```bash
mkdir build
cd build
cmake -Dunitree_legged_sdk_PYTHON=ON ..
make
```

## Install
```bash
cd /pathto/unitree_legged_sdk
pip install .
```

if you use conda or miniconda, you can also install as following:
```bash
cd /pathto/unitree_legged_sdk
python3 setup.py install
```

## Tests
**test**
```bash
cd /pathto/unitree_legged_sdk/examples_py
python3 example_walk.py
```
