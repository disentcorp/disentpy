.. Disent Client for Python3 documentation master file, created by
   sphinx-quickstart on Sat Jun 11 15:52:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :numbered:
   :maxdepth: 5
   :caption: Docs:
   
.. sectnum::

Getting Started
==================

.. code-block:: console

   (venv) $ pip install disentpy

.. code-block:: python3

   >>> import disent
   >>> disent.example()
   Downloaded........ 134.0 KiB done.
         TCK   MNY        YRS        IV    T                   DT
   0    AAPL  0.00   0.079452  0.791190   1M  2022-07-11T00:00:00
   1    AAPL  0.00   0.164384  0.740517   2M  2022-08-11T00:00:00
   ..    ...   ...        ...       ...  ...                  ...
   718  AAPL  2.95   7.002740  0.303335   7Y  2029-06-11T00:00:00
   719  AAPL  2.95  10.005479  0.303335  10Y  2032-06-11T00:00:00

   [720 rows x 6 columns]

When using :code:`disent.example()` you'll get a :code:`pandas.DataFrame` from Disent's demo volatility surface for Apple on recent data from the public domain. This is a wrapper on :code:`disent.hub`.

Demo Functionality
==================

.. warning::

   Data is provided for demonstration purposes and sourced from the public domain.

Equity Volatility
------------------

.. Observable market quotes
.. ~~~~~~~~~~~~~~~~~~~~~~~~~

.. *(todo)*

.. Fully inverted surface (black implied)
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. *(todo)*

.. Normalized OTC surface
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~

When using :code:`disent.hub()` you'll get a :code:`pandas.DataFrame`:

.. code:: python3

   >>> model="DEMO_EQD_VOLS"
   >>> ticker = 'AAPL'
   >>> model_args = {'ticker':ticker}
   >>> df = disent.hub(model,model_args,env='disent-cloud')

.. table::
   :align: center


   +------+------+-----------+----------+-----+---------------------+
   | TCK  | MNY  | YRS       | IV       | T   | DT                  |
   +======+======+===========+==========+=====+=====================+
   | AAPL | 0.00 | 0.079452  | 0.791190 | 1M  | 2022-07-11T00:00:00 |
   +------+------+-----------+----------+-----+---------------------+
   | AAPL | 0.00 | 0.164384  | 0.740517 | 2M  | 2022-08-11T00:00:00 |
   +------+------+-----------+----------+-----+---------------------+
   | ...  | ...  | ...       | ...      | ... | ...                 |
   +------+------+-----------+----------+-----+---------------------+
   | AAPL | 2.95 | 7.002740  | 0.303335 | 7Y  | 2029-06-11T00:00:00 |
   +------+------+-----------+----------+-----+---------------------+
   | AAPL | 2.95 | 10.005479 | 0.303335 | 10Y | 2032-06-11T00:00:00 |
   +------+------+-----------+----------+-----+---------------------+




.. note::
   
   Various configurations and settings are available for enterprise subscribers. Below is describing the specifics of the **DEMO_EQD_VOLS** default model.

*Descriptive columns*

.. _OCC: https://www.theocc.com/Market-Data/Market-Data-Reports/Series-and-Trading-Data/Directory-of-Listed-Products
  
- :math:`\text{TCK}` are the option contract root symbols using standard exchange root codes (`OCC`_) root symbols.

- :math:`\text{MNY}` are defined as :math:`f(S,K) = \displaystyle\frac{K}{S}` bucketed into a pre-defined moneyness scale.

- :math:`\text{T}` are rolling contract maturities, i.e. durations/tenors/time periods (akin to :code:`datetime.timedelta`), bucketed into a classic tenor scale:

.. list-table::
   :align: center

   * - 1M
     - 3M
     - 6M
     - 1Y
     - 5Y
     - 10Y

Across the Disent platform rolling tenors include two helpers:

.. _ISO8601: https://en.wikipedia.org/wiki/ISO_8601

- :math:`\text{DT}` are expressed as `ISO8601`_ strings as :math:`\text{ACT}` days from today. Use :code:`pandas.to_datetime()` for conversion.

- :math:`\text{YRS}` are the year fractions from today and :math:`\text{DT}` using :math:`\text{ACT/365}` convention.


*Evalauted columns*

.. _Black-Scholes-Merton: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model
.. _spline-based interpolation: https://en.wikipedia.org/wiki/Spline_interpolation

- :math:`\text{IV}` is the implied volatlity. It is derived using a Disent-specific implementation of `Black-Scholes-Merton`_ using `spline-based interpolation`_.


Environments
==================

Environment List
------------------

* public (default)

List current environment
------------------------

.. code-block:: python3

   >>> disent.env.get()
   public

Change (set) environment
------------------------

.. code-block:: python3

   >>> disent.set.set('prod')
   public --> prod


.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

