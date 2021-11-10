import setuptools

setuptools.setup(
    name="SocProofAPI",
    version="1.0.0",
    author="infqq",
    description="Wrapper for soc-proof API",
    url="https://github.com/Infqq/SocProofAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.25.1',
    ],
)
