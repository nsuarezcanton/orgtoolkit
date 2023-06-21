from setuptools import setup

setup(
    name="orgtoolkit",
    version="0.0.1",
    py_modules=["orgtoolkit"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "orgtoolkit = orgtoolkit:cli",
        ],
    },
)
