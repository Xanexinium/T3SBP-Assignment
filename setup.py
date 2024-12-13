from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ScorestreamPy_lib",  
    version="0.0.1",  
    author="Markiian Prysukhin",
    author_email="edgetechnics@egmail.com",
    description="A Python library for managing a scoreboard with match tracking, score updates, and thread safety.", 
    long_description=long_description,  
    long_description_content_type="text/markdown", 
    url="https://github.com/yourusername/ScorestreamPy_lib",
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",  
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",  
    install_requires=[
        "pytest>=7.4.0",  
        "coverage>=7.0.0",  
    ],
    extras_require={
        "dev": ["flake8"],  
    },
    project_urls={
        "Bug Tracker": "https://github.com/Xanexinium/T3SBP-Assignment/issues",
        "Documentation": "https://github.com/Xanexinium/T3SBP-Assignment",
        "Source Code": "https://github.com/Xanexinium/T3SBP-Assignment",
    },
)
