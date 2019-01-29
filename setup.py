import os

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

cli_path = "cli-tools/"
cli_files = [os.path.join(cli_path, file) for file in os.listdir(cli_path)]

setup(
    name="deepsurf",
    version="0.1.1",
    description="Applying deep learning techniques to beach cam data",
    author="HowardRiddiough",
    long_description=long_description,
    author_email="howardriddiough@gmail.com",
    packages=["deepsurf"],
    install_requires=[
        "skyfield==1.9"
    ],
    extras_require={
        "test": {"flake8==3.6.0", "pep8-naming==0.7.0", "pytest==3.7.0", "pytest-cov"},
    },
    scripts=cli_files,
)
