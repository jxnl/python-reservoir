from distutils.core import setup

setup(
    name="Reservoir",
    version='0.1.2',
    author='Jason Liu',
    author_email='jx5liu@uwaterloo.ca',
    packages=['reservoir'],
    url='https://github.com/jxnl/python-reservoir',
    license='LICENSE.txt',
    description="""Collection of reservoir sampling algorithms. Includes uniform and exponential samplers and command line interface for sampling files and data streams.""",
    long_description=open("README.md").read(),
    entry_points={'console_scripts': ['sample=reservoir.command:main']},
)
