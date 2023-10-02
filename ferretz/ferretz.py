# ferretz.py
from pathlib import Path
from random import choice
import os


def greet_user():
    greetings = [
        "🦡 Hey there, hooman! Ready to code?",
        "🦡 What's cookin', good lookin'?",
        "🦡 Look who's back for more coding fun!"
    ]
    print(choice(greetings))


def create_directory_structure(package_name, author, email, target_dir):
    root = Path(target_dir) / package_name
    root.mkdir(parents=True, exist_ok=True)

    package_dir = root / package_name
    package_dir.mkdir()
    setup_py = root / 'setup.py'

    modules = ['constants.py', 'display.py', 'download.py', 'file_utilities.py',
               'image_conversion.py', 'image_processing.py', '__init__.py',
               'input_validation.py', package_name+'.py', 'resources.py']

    for module in modules:
        module_path = package_dir / module
        with open(module_path, 'w') as f:
            preamble = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
.. module:: {module[:-3]}
   :platform: Unix, Windows
   :synopsis: A module for {package_name}.

.. moduleauthor:: {author} <{email}>

This module is part of the {package_name} package.
'''

# Your code here
"""
            f.write(preamble)

    with open(setup_py, 'w') as f:
        content = f"""from setuptools import setup, find_packages

setup(
    name='{package_name}',
    version='0.1',
    packages=find_packages(),
    author='{author}',
    author_email='{email}',
    url='',  # Add your package's homepage URL here
    description='',  # Add a short description of the package here
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],  # List your package's dependencies here
    classifiers=[
        # Choose your audience and license, etc.
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
)
"""
        f.write(content)


def create_new_package():
    while True:
        package_name = input("📦 What's the name of the new package? (Remember to end it with 'z') ")
        if package_name.endswith('z'):
            break
        else:
            print("🦡 Oops! The package name should end with a 'z'. Try again.")

    author = input("👩‍💻 Who's the author? ")
    email = input("📧 Author's email? ")

    while True:
        target_dir = input("🗂 Where would you like to create the new package? (Provide the full path) ")
        if Path(target_dir).exists():
            break
        else:
            print("🦡 Oops! That directory doesn't exist. Try again.")

    create_directory_structure(package_name, author, email, target_dir)
    print("🦡 Yay! Your new package '{}' has been successfully created!".format(package_name))


def main():
    greet_user()
    action = input("What would you like to do today? (type 'new' to create a new package) 🎬 ")

    if action == 'new':
        create_new_package()


if __name__ == "__main__":
    main()
