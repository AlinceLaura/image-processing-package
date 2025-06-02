from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ALM_test",
    version = "0.0.3",
    author="Alince Laura",
    description = "Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlinceLaura/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
    )
