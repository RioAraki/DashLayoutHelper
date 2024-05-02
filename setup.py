from setuptools import setup, find_packages

setup(
    name='DashLayoutHelper',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        pandas,
        dash,
        dash_bootstrap_components
    ],
    author='Yue Li',
    author_email='lhzuigao@hotmail.com',
    description='Helper class for Dash UI programming',
)