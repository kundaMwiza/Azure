from setuptools import setup, find_packages

setup(
    name = "simple_package"
    ,version = "1.0.0"
    ,description = "something shorter than long description"
    ,long_description = "something shorter than description"
    ,url = ""
    ,author = "Mwiza Kunda"
    ,license = "something"
    ,packages = find_packages()
    ,install_requires = [
        "numpy"
        ,"pandas"
        ,"scipy"
    ]
    ,python_requires = ">=3.6"
    ,setup_requires = ["pytest_runner"]
    ,tests_require = ["pytest", "pytest-cov"]
)