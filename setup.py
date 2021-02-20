import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gravitational",
    version="0.2.0",
    author="Behrouz Safari",
    author_email="behrouz.safari@gmail.com",
    description="A package for gravitational simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/behrouzz/gravitational",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["gravitational"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib"],
    python_requires='>=3.6',
)
