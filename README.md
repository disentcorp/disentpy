
# disentpy

Python client for Disent's API framework.

## Installation

Install using `pip`

``` shell
pip install disentpy
```

## Usage

``` python
import disent
model="VOLS_DEMO"
key="AAPL"
df = disent.md(model=model,key=key)
```

## Documentation

Latest documentation is hosted on [read the docs](https://disentpy.readthedocs.io/en/latest/).

### Requirements

Using disentpy requires the following packages:

-   pandas>=1.0
-   requests>=2.19.0


### Install latest development version

``` shell
pip install git+http://github.com/disentcorp/disent_pip.git
```

or

``` shell
git clone pip install https://github.com/disentcorp/disent_pip.git
cd disentpy
python setup.py install
```