from setuptools import setup, find_packages

setup(
    name="my_eda_cli",
    version="0.1.0",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "pandas",
        "click",
        "jinja2",
        "pyarrow"
    ],
    entry_points={
        "console_scripts": [
            "eda-report=my_eda_cli.cli:main",
        ],
    },
)