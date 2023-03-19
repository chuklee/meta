
# META

## Authors

- [@chuklee](https://github.com/chuklee)


## Project Overview

META is a Python project that aims to create a virtual trading platform where users can create their own bases and connect their own neurones to it. The project is composed of two main classes: Base and Neurone.

The Base class is responsible for creating and managing the bases, which have a certain amount of value (taux_base) and a number of neurones. Each base has its own unique identifier, username and password.

The Neurone class represents the users that connect to the bases. They have their own username and password, and they can vote and give confidence points to other neurones. Neurones also have a value (pt_valeur) and a performance (rendement).

## Getting Started
To run the project, you will need to have Python 3 installed on your computer. The project also requires the mysql-connector-python package to be installed. You can install this package by running the following command:
```bash
    pip install mysql-connector-python
```
Once you have installed the necessary dependencies, you can run the project by running the META.py file.

## Usage
The project can be used to create virtual trading platforms where users can create their own bases and connect their own neurones to it. Users can vote and give confidence points to other neurones, and each neurone has a value and a performance.

The project can be run from the command line, and it provides a menu-based interface for interacting with the bases and neurones.
