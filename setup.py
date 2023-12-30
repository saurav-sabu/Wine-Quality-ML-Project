from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine-Quality-ML-Project"
AUTHOR_USER_NAME = "saurav-sabu"
SRC_REPO = "Wine-Quality-ML-Project"
AUTHOR_EMAIL = "saurav.sabu9@gmail.com"

setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="ML Project on finding Wine Quality",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues" 
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")
)
