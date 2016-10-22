from setuptools import setup

# Based on code from:
# http://python-packaging.readthedocs.io/en/latest/minimal.html

# Run using the command:
#    $pip install .

setup(name='numerical_methods',
      version='0.1',
      description='Numerical methods in python',
      url='https://github.com/MatthewPeterKelly/numerical-methods-in-python',
      author='Matthew Peter Kelly',
      author_email='matthew.kelly2@gmail.com',
      license='MIT',
      packages=['numerical_methods'],
      install_requires=[
          'matplotlib',
          'numpy'
      ],
      zip_safe=False)
