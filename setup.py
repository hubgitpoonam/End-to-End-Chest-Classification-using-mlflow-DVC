import setuptools

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"
REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR = "poonsmkumari428"
PACKAGE_NAME = "cnnClassifier"
AUTHOR_EMAIL = "poonamkumarirt428@gmail.com"

# Setup configuration
setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for a CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
