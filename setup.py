from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pystratis',
    version='1.0.0.6',
    description='Official python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.',
    author='Tjaden Froyda',
    license='MIT',
    packages=[x for x in find_packages() if 'tests' not in x],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/stratisproject/pystratis',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='stratis, cirrus, pystratis, smartcontracts, blockchain',
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'pydantic>=1.8.2',
        'base58',
        'base58check',
        'bech32',
        'pysha3'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest_mock',
            'pytest_order',
            'coverage',
            'ecdsa',
            'mnemonic'
        ]
    }
)
