'''
Created on Aug 20, 2010

@author: John Salvatier
'''
import setuptools
print setuptools.find_packages()

setuptools.setup(name     = "numpydb",
                 version  = ".1",
                 packages = setuptools.find_packages(),
                 install_requires = ['numpy'])