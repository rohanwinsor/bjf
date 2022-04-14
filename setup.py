from setuptools import setup, find_packages


install_requires = [
    "click==8.1.0",
]


setup(
    name="jf",
    description="Simple in-place JSON Formatter",
    author="rohan winsor",
    author_email="rohan.w.charles@gmail.com",
    url="https://github.com/rohanwinsor/jf",
    install_requires=install_requires,
    packages=find_packages(),
    license="MIT",
)
