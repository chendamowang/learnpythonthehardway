# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description' : 'My project',
    'author' : 'ChenWeiZhe',
    'author_email' : '249883376@qq.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config) 
