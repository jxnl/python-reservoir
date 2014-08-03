from distutils.core import setup

setup(
    name="Reservoir",
    version='0.1.1',
    author='Jason Liu',
    author_email='jx5liu@uwaterloo.ca',
    packages=['reservoir'],
    url='https://github.com/jxnl/python-reservoir',
    license='LICENSE.txt',
    description='Generate k samples from any iterable or data stream.',
    entry_points={'console_scripts': ['res-sample=reservoir.reservoir:main']},
    install_requires=[
        "argparse == 1.2.1",
    ],
)
