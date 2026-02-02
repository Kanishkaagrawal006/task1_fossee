# General Tree Package

A Python package to create and manipulate general trees (nodes with any number of children).

**This package is built and tested using Python 3.12 and must be used inside a virtual environment.**

## Features

* Create a general tree
* Add nodes
* Remove nodes
* Print tree structure
* Compatible with YAML for saving/loading trees 

## Requirements

* Python 3.12
* pip (for installing packages)
* Virtual environment (strongly recommended)

## Setup Instructions

### Create a Python 3.12 virtual environment

### Windows
              python -m venv venv

### macOS/Linux
          python3.12 -m venv venv


### Activate the virtual environment

### Windows
          venv\Scripts\activate

### macOS/Linux
     source venv/bin/activate

### Install the package

     pip install git+https://github.com/Kanishkaagrawal006/task1_fossee.git
### Install dependencies

    pip install -r requirements.txt


### Verify installation

    python -m pip list

### Usage

    from general_tree import *

    # Example: create a root node
    root = Node("Root")

     # Add children
    root.add_child("Child 1")
     root.add_child("Child 2")


    root.print_tree()


⚠️ Make sure your virtual environment is active and Python 3.12 is being used. Otherwise, the package may not work.