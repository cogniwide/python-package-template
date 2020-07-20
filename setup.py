from setuptools import setup, find_packages

import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


install_requires = [
    'requests==2.22.0',
]

setup(
    name='cogniwide',
    version='1.0',
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests", "venv", "examples"]),
    entry_points={"console_scripts": ["cogniwide=cogniwide.__main__:main"]},
    author="Alfred Francis",
    author_email="alfred@cogniwide.com",
    description="CogniDocs core module",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://cogniwide.com/products/cognidiscovery",
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
