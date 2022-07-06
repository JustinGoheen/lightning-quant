from setuptools import setup
from setuptools import find_packages
from pathlib import Path

console_scripts = """
[console_scripts]
pod=lightning_quant.cli.console:main
"""

rootdir = Path(__file__).parent
long_description = (rootdir / "README.md").read_text()

setup(
    name="lightning-quant",
    version="0.0.1",
    description="A LightningAI framework for the Interactive Brokers TWS API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinGoheen/lightning-quant",
    author="Justin Goheen",
    license="Apache 2.0",
    install_requires=[],
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points=console_scripts,
)
