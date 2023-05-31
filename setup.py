from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='shortest_path_python',
    version='0.0.1',
    description='Simple shortest path finder',
    long_description=readme,
    author='nate200',
    author_email='email of the author',
    url='https://github.com/nate200/shortest_path_python',
    packages=find_packages(exclude=('tests', 'docs'))
)

