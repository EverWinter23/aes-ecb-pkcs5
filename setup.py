from setuptools import find_packages, setup

tests_require = [
    "pytest>=5.1.2",
    "pytest-cov==2.7.1",
]

dev_requires = [
    "black>=22.6.0",
    "flake8>=5.0.4",
] + tests_require

with open("README.md", "r") as desc:
    long_description = desc.read()

setup(
    name="aes-ecb-pkcs5",
    version="0.0.1a",
    description="AES/ECB/PKCS5 cipher encryption/decryption using python3 standard library.",
    long_description_content_type='text/markdown',
    url="https://github.com/EverWinter23/aes-ecb-pkcs5",
    long_description=long_description,
    keywords="aes ecb pkcs5 encryption decryption java aes-ecb",
    packages=find_packages(exclude=["tests"]),
    author="Rishabh Mehta",
    author_email="eternal.blizzard23@gmail.com",
    install_requires=[
        "cryptography>=37.0.4",
    ],
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "dev": dev_requires,
    },
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
)
