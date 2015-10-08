from setuptools import find_packages, setup

from sorethumb import __version__ as VERSION


setup(
    name='sorethumb',
    packages=find_packages(exclude=['docs']),
    version=VERSION,
    description='Thumbnail image processing, with Django integration',
    author='Will McGugan',
    author_email='will@willmcgugan.com',
    maintainer='Will McGugan',
    maintainer_email='will@willmcgugan.com',
    url='https://github.com/willmcgugan/sorethumb',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['pillow>=3.0.0'],
)
