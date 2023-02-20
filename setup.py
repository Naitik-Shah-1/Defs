"""
Imports:
    `setup` function from the `setuptools` module
"""

from setuptools import setup

setup(
    name="defs",
    version="0.0.1",
    description="This is a pkg containing basic definitions which are used often.",
    author="Naitik Shah",
    author_email="NaitikShah.Work@outlook.com",
    maintainer="Naitik Shah",
    maintainer_email="NaitikShah.Work@outlook.com",
    packages=["defs"],
    package_dir={"": "src"},
)
