from setuptools import setup

setup(
    name='binaryrepr',
    version='0.1',
    py_modules=['binaryrepr'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        binaryrepr=binaryrepr:binaryrepr
    ''',
)
