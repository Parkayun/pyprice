pyprice
=======


Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install
   
or can use pip

.. sourcecode:: bash

   ~ $ pip install pyprice

Quick start
-----------

Terminal

.. sourcecode:: bash

   $ pyprice kospi
   Keyword: KOSPI
   Value: 2,087.89
   Change: 14.98, 0.72%
   Market: Korea Stock Exchange (Koscom)
  
   $ pyprice search face
   Keyword: FACEX
   Name: Frost Growth Equity Fund Investor Class Shares

   Keyword: FB
   Name: Facebook

Python

.. sourcecode:: python

   >>> from pyprice.index import search
   >>> search('samsung')
   [[{'c': 'US', 'd': 'SSNLF', 'it': 'CS', 's': 'SSNLF', 'cnn': 'SSNLF', 'n': 'Samsung Electronics Co Ltd', 'lt': 'IssueNameFast.5.0', 'e': 'Grey Market', 'w': '260239'}]]
   