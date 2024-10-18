#to find constructor file and setup the src folder as local package.
from setuptools import find_packages, setup

setup(
    name = "Zomato Chatbot",
    version= "0.0.0",
    author= "apoorv",
    author_email= "apoorvsinghnegi18@gmail.com",
    packages= find_packages(),
    install_requires=[]
)