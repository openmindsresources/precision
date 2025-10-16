from setuptools import setup, find_packages

setup(
    name="precision",
    version="0.1.0",
    packages=find_packages(),
    package_data={"precision": ["*.so"]},
    # required dependencies
    install_requires=[
        "matplotlib",
        "pandas",
        "pymc_marketing",
        "seaborn"
    ],
)
