from setuptools import find_packages, setup

setup(
    name="ECON320_lib",
    packages=find_packages(include=["ECON320_lib"]),
    version="0.1.2",
    description="ECON320 Python Library",
    author="James Minkyu Song",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    # test_suite="test_ECON320_lib",
)
