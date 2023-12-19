import setuptools

__version__="0.0.0"
AUTHOR_NAME="Abhikkumar619"
AUTHOR_EMAIL="abisheky194@gmail.com"
REPO_NAME="Wafer_sensor_project"
SRC_REPO="wafer_project"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_NAME,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)