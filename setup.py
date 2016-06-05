from distutils.core import setup

setup(
    name='python-nomad',
    version='0.0.1',
    install_requires=['requests'],
    packages=['nomad', 'nomad.api'],
    url='http://github.com/jrxfive/python-nomad',
    license='MIT',
    author='jrxfive',
    author_email='jrxfive@gmail.com',
    description='HTTP API Wrapper for Hashicorp Nomad',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nomad hashicorp apiwrapper',
)
