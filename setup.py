from setuptools import setup, find_packages

with open('requirements.txt', 'rb') as f:
    content = f.readlines()

requirements = [x.strip() for x in content]

setup(name='bank_fraud',
      version='0.0.1',
      packages=find_packages())
