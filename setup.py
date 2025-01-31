"""Nomad Python Library"""
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-nomad',
    version='2.1.0',
    install_requires=['requests'],
    packages=['nomad', 'nomad.api'],
    url='http://github.com/jrxfive/python-nomad',
    license='MIT',
    author='jrxfive',
    author_email='jrxfive@gmail.com',
    description='Client library for Hashicorp Nomad',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='nomad hashicorp client',
)
