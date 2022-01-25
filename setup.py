import os
import setuptools

from randluck import __version__


readme_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
with open(readme_filepath, "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="randluck",
    version=__version__,
    author="Tong Zhu",
    author_email="tzhu1997@outlook.com",
    description="A toolkit for selecting random seed with luck",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Spico197/random-luck",
    packages=setuptools.find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "sxtwl>=2.0.4"
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'black',
            'coverage'
        ]
    }
)
