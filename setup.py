# to consider all the folder a package we use setup
# To download in local folder

from setuptools import find_packages, setup


setup(
    name= "Generative AI Project",
    version= "0.0.0",
    author="Chanchal",
    author_email="entbabby73@gmail.com",
    packages=find_packages(),
    install_requries = []
)