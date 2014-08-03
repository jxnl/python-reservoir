from distutils.core import setup

setup(
    name="Reservoir",
    version='0.1.0',
    author='Jason Liu',
    author_email='jx5liu@uwaterloo.ca',
    packages=['reservoir'],
    scripts=['bin/reservoir-sample.py'],
    url='https://github.com/jxnl/python-reservoir',
    license='LICENSE.txt',
    description='Generate a sample of elements from any interable',
    long_description=open('README.md').read(),
    entry_points={'console_scripts': ['samplepy = reservoir.reservoir:main']},
    install_requires=[
        "argparse == 1.2.1",
    ],
)
