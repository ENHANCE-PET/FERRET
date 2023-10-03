# setup.py for ferretz
from setuptools import setup, find_packages

setup(
    name='ferretz',
    version='0.2',
    description='A Python package to create "enhance.pet" compliant package folder structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lalith Kumar Shiyam Sundar',
    author_email='lalith.shiyamsundar@meduniwien.ac.at',
    url='https://github.com/LalithShiyam/ferretz',  # Replace with your GitHub URL
    license='MIT',  # Replace with your license
    packages=find_packages(exclude=['template_modules']),
    package_data={'ferretz': ['template_modules/*.py']},
    entry_points={
        'console_scripts': ['ferretz=ferretz.ferretz:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='enhance.pet, package creation, Python',
    install_requires=[
        # List your package dependencies here
    ],
)
