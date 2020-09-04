import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="howfairis",
    entry_points={
        "console_scripts": ["howfairis=howfairis:main"],
    },
    version="0.1.0",
    description="Python package to analyze compliance with fair-software.eu recommendations",
    long_description=readme + "\n\n",
    author="https://github.com/jspaaks",
    author_email="j.spaaks@esciencecenter.nl",
    url="https://github.com/fair-software/howfairis",
    packages=[
        "howfairis",
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="howfairis",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    install_requires=[
        "requests"
    ],
    setup_requires=[
        # dependency for `python setup.py test`
        "pytest-runner"
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pycodestyle",
    ],
    extras_require={
        "dev":  [
            "prospector[with_pyroma]",
            "yapf",
            "isort",
            "bumpversion"
        ],
    },
    data_files=[]
)
