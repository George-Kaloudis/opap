import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opap",
    version="1.0.2",
    author="George Kaloudis",
    author_email="georgekal123@gmail.com",
    description="An api that collects data from opap.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/George-Kaloudis/opap",
    packages=setuptools.find_packages(exclude=[".gitignore", ".idea", "docs"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)