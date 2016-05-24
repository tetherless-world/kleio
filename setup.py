from setuptools import setup
import re
import pypandoc

try:
    description = pypandoc.convert('README.md', 'rst', format='md')
except (IOError, ImportError):
    description = open('README.md').read()


def find_version(filename):
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)


version = find_version('kleio/__init__.py')

packages = [
    'kleio'
]

setup(
    name='kleio',
    version=version,
    py_modules=['kleio'],
    author='Stephan Zednik',
    author_email='zednis2@rpi.edu',
    url='http://github.com/tetherless-world/kleio',
    description='A simple python implementation of the W3C PROV data model',
    long_description=description,
    install_requires=['rdflib', 'rdflib-jsonld', 'isodate'],
    license='MIT',
    packages=packages,
    keywords='provenance PROV PROV-O rdf',
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3']
)
