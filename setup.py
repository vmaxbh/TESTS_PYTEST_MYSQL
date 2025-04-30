from setuptools import setup, find_packages

setup(
    name="mysql_tests",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytest==7.4.0',
        'mysql-connector-python==8.0.33',
        'python-dotenv==1.0.0'
    ],
)
