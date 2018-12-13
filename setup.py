import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hbapi",
    version="1.0.0",
    author="George Kaloudis",
    author_email="georgekal123@gmail.com",
    description="An api that collects the bundles, and what they contain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/George-Kaloudis/hbapi",
    packages=setuptools.find_packages(exclude=[".gitignore", ".idea", "docs", "AUTHORS.rst"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)