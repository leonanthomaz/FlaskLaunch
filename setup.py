from setuptools import setup, find_packages

setup(
    name="flasklaunch",
    version="0.1.1",
    author="Leonan Thomaz",
    author_email="leonan.thomaz@gmail.com",
    description="A tool to quickly launch Flask projects",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leonanthomaz/flasklaunch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "flask",
        "dynaconf",
        "pyyaml",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "flasklaunch = flasklaunch.cli:cli",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/leonanthomaz/flasklaunch/issues",
        "Documentation": "https://github.com/leonanthomaz/flasklaunch/wiki",
        "Source Code": "https://github.com/leonanthomaz/flasklaunch",
    },
)
