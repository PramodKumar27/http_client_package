from setuptools import find_packages, setup

setup(
    name='http_client_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.7.4'
    ],
    description='A reusable and simple HTTP client wrapper using aiohttp for making asynchronous HTTP requests.',
    author='Pramod Kumar',
    author_email='pramod.kumar@agbeindia.com',
    url='https://github.com/PramodKumar27/http_client_package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
