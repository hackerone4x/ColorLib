from distutils.core import setup

setup(
    # Application name:
    name="ColorsLib",

    # Version number (initial):
    version="1.1.0",

    # Application author details:
    author="Abdulrahman Ayman",
    author_email="hatcyperse@gmail.com",

    # Packages
    packages=["colorsLib"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/ColorsLib_110/",

    #
    # license="LICENSE.txt",
    description="Colors Lib For Hackers",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "random",
    ],
)
