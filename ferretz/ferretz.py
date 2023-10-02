from pathlib import Path
from random import choice

# ANSI Escape Codes for color output
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'


def greet_user():
    greetings = [
        f"{GREEN}🦡 Hey there, hooman! Ready to code?{RESET}",
        f"{GREEN}🦡 What's cookin', good lookin'?{RESET}",
        f"{GREEN}🦡 Look who's back for more coding fun!{RESET}"
    ]
    print(choice(greetings))


def create_directory_structure(package_name, author, email, target_dir):
    print(f"{BLUE}🦡 Creating your lair... Ahem, I mean your package directory! 📦{RESET}")

    root = Path(target_dir) / package_name
    root.mkdir(parents=True, exist_ok=True)
    package_dir = root / package_name
    package_dir.mkdir(exist_ok=True)
    setup_py = root / 'setup.py'

    modules = [
        'constants.py', 'display.py', 'download.py', 'file_utilities.py',
        'image_conversion.py', 'image_processing.py', '__init__.py',
        'input_validation.py', f"{package_name}.py", 'resources.py'
    ]

    summary = []

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
        summary.append(f"Created: {module_path}")

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
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
)
"""
        f.write(content)
        summary.append(f"Created: {setup_py}")

    print(f"{GREEN}🦡 Your new den... er, package, is ready to rumble! 🎉{RESET}")
    return summary


def post_generation_summary(summary):
    print(f"{BLUE}🦡 Here's a sneak peek at what I've dug up for you: 🐾{RESET}")
    for item in summary:
        print(f"  - {item}")
    print("Next steps:")
    print("  1️⃣ Review the generated files.")
    print("  2️⃣ Populate the modules with your code.")
    print("  3️⃣ Install dependencies if necessary.")
    print("  4️⃣ Test your package.")
    print("  5️⃣ Create a README.md and other documentation.")
    print("  6️⃣ Run 'python setup.py sdist bdist_wheel' to package your project.")
    print("  7️⃣ Install twine if you haven't: 'pip install twine'")
    print("  8️⃣ Run 'twine upload dist/*' to upload your package to PyPI.")


def create_new_package():
    while True:
        package_name = input(f"{BLUE}🦡 What's the name of the new package? (Must end with 'z') 📦{RESET}")
        if package_name.endswith('z'):
            break
        else:
            print(f"{RED}🦡 Oopsie! Your package name should end with a 'z'. Retry! 🚫{RESET}")

    author = input(f"{BLUE}🦡 Who's the genius behind this package? (Author's name) 👩‍💻{RESET}")
    email = input(f"{BLUE}🦡 Got an email, smarty-pants? 📧{RESET}")

    while True:
        target_dir = input(f"{BLUE}🦡 Where should I dig the new hole... um, I mean, where should the package be created? (Provide the full path) 🗂{RESET}")
        if Path(target_dir).exists():
            break
        else:
            print(f"{RED}🦡 Oops! That hole doesn't exist... I mean, directory! Try again. 🚫{RESET}")

    summary = create_directory_structure(package_name, author, email, target_dir)
    post_generation_summary(summary)


def main():
    greet_user()
    action = input(f"{BLUE}🦡 What's on the agenda today, boss? ('new' to create a new package) 🎬{RESET}")

    if action.lower() == 'new':
        create_new_package()
    else:
        print(f"{RED}🦡 Aww, shucks! I don't know that command. 🚫{RESET}")

if __name__ == "__main__":
    main()

