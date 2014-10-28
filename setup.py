from setuptools import setup

setup(
    name='nagios-plugin-check-aws-vpn-status',
    version='0.0.2',
    packages=[],
    scripts=['bin/check-aws-vpn-status'],
    include_package_data=True,
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    install_requires=['boto==2.31.1'],
    long_description=open('README.md').read(),
)