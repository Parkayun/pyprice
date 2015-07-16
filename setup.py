"""
pyprice
-------
stock price index wrapper.
"""

from os import path
from setuptools import setup

from pyprice import VERSION


long_description = open(
    path.join(
        path.dirname(__file__),
        'README.rst'
    )
).read()

setup(
    name='pyprice',
    version=VERSION,
    url='https://github.com/Parkayun/pyprice',
    license='MIT',
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='stock price index wrapper.',
    long_description=long_description,
    packages=['pyprice'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points={
        'console_scripts': [
            'pyprice=pyprice.cli:runner',
        ],
    },
)