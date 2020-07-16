import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lambdata-DSPT6-JTC",  # Replace with your own username
    version="0.0.4",
    author="Jordan Carlisle",
    author_email="jordantcarlisle@gmail.com",
    description="This is a small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordantcarlisle/Lambdata-DSPT6-JTC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
