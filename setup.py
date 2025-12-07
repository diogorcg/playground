import json
from pathlib import Path

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

BASE_DIR = Path(__file__).parent

GITHUB_URL = "@git+ssh://git@github.com:diogorcg/"

# Load packages from requirements.txt
with open("Pipfile.lock") as pip_file:
    pipfile_json = json.load(pip_file)

locked_requirements = [
    package + detail.get("version", "")
    for package, detail in pipfile_json["default"].items()
]

develop_requirements = [
    package + detail.get("version", "")
    for package, detail in pipfile_json["develop"].items()
]

setup(
    name="playground",
    version="0.1.0",
    description="Diogo's playground",
    author="Diogo Gonçalves",
    author_email="diogorcgoncalves@gmail.com",
    python_requires=">=3.10",
    long_description=long_description,
    packages=find_packages(exclude=("tests", "resources")),
    install_requires=locked_requirements,
    extras_require={
        "dev": develop_requirements,
    },
    entry_points={
        "console_scripts": [
            "Playground = epl_fantasy.main:app",
        ],
    },
)
