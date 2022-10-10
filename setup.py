from setuptools import setup

setup(
    name='django_exception_handler',
    version='0.0.1',
    author='Shaghayegh Ghorbanpoor',
    author_email='ghorbanpoor.shaghayegh@gmail.com',
    packages=['django_exception_handler'],
    # scripts=['bin/script1', 'bin/script2'],
    # url='http://pypi.python.org/pypi/PackageName/',
    # license='LICENSE.txt',
    description='An awesome package that handle exceptions',
    long_description=open('README.md').read(),
    install_requires=[
        'Django'
    ],
)
