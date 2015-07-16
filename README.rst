pyprice
=======


Installation
-------------

.. sourcecode:: bash

   $ python setup.py install
   
or can use pip

.. sourcecode:: bash

   $ pip install pyprice

Quick start
-----------

Terminal

.. sourcecode:: bash

   $ pyprice kospi
   KOREA SE KOSPI IDX / KOSPI
   Current Price: 2,087.89 (14.98, 0.72%)
   Market: Korea Stock Exchange (Koscom)
  
   $ pyprice search face
   Name: Frost Growth Equity Fund Investor Class Shares
   Keyword: FACEX
   Market: NASDAQ

   Name: Facebook
   Keyword: FB
   Market: NASDAQ

Python

.. sourcecode:: python

   >>> from pyprice.index import search
   >>> search('samsung')
   [[{'c': 'US', 'd': 'SSNLF', 'it': 'CS', 's': 'SSNLF', 'cnn': 'SSNLF', 'n': 'Samsung Electronics Co Ltd', 'lt': 'IssueNameFast.5.0', 'e': 'Grey Market', 'w': '260239'}]]
   