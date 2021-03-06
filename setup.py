# Standard Library
from os.path import abspath, dirname, join

# external
from setuptools import find_packages, setup

CUR_DIR = dirname(abspath(__file__))
INIT_FILE = join(CUR_DIR, 'stix2elevator', '__init__.py')
VERSION_FILE = join(CUR_DIR, 'stix2elevator', 'version.py')


def get_version():
    with open(VERSION_FILE) as f:
        for line in f:
            if not line.startswith("__version__"):
                continue

            version = line.split()[-1].strip('"')
            return version

        raise AttributeError("Package does not have a __version__")


with open('README.rst') as f:
    readme = f.read()

setup(
    name='stix2-elevator',
    version=get_version(),
    description='Utility to upgrade STIX 1.X and CybOX content to STIX 2.X',
    long_description=readme,
    url='https://oasis-open.github.io/cti-documentation/',
    author='OASIS Cyber Threat Intelligence Technical Committee',
    author_email='cti-users@lists.oasis-open.org',
    maintainer='Rich Piazza',
    maintainer_email='rpiazza@mitre.org',
    packages=find_packages(exclude=['*.test', '*.test.*']),
    install_requires=[
        'pycountry>=19.8.18',
        'netaddr',
        'stix>=1.1.1.9,<1.2.1.0',
        'stix2-validator>=2.0.0.dev3',
        'stixmarx>=1.0.6',
        'six>=1.12.0',
        'stix2'
    ],
    entry_points={
        'console_scripts': [
            'stix2_elevator = stix2elevator.cli:main',
            'stix_stepper = stix2elevator.stix_stepper:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    keywords='stix stix2 json xml cti cyber threat intelligence',
    project_urls={
        'Documentation': 'https://stix2-elevator.readthedocs.io/',
        'Source Code': 'https://github.com/oasis-open/cti-stix-elevator/',
        'Bug Tracker': 'https://github.com/oasis-open/cti-stix-elevator/issues/',
    },
    extras_require={
        'dev': [
            'bumpversion',
            'pre-commit',
        ],
        'test': [
            'coverage',
            'pytest',
            'pytest-cov',
            'tox',
        ],
        'docs': [
            'sphinx',
            'sphinx-prompt',
        ],
    },
)
