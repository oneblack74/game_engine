# setup.py
from setuptools import setup, find_packages

setup(
    name='game_engine',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    description='Un moteur de jeu en 2D avec Pygame',
    author='Brissy Axel',
    author_email='axelbrissy0804@gmail.com',
    url='https://github.com/oneblack74/game_engine',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
