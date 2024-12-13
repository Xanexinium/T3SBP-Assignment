from setuptools import setup, find_packages

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ScorestreamPy_lib",  # Package name (used when installing via pip)
    version="0.1.0",  # Initial version
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email
    description="A Python library for managing a scoreboard with match tracking, score updates, and thread safety.",  # Short description
    long_description=long_description,  # Detailed description from README
    long_description_content_type="text/markdown",  # Markdown formatting
    url="https://github.com/yourusername/ScorestreamPy_lib",  # Link to your repository
    packages=find_packages(),  # Automatically discover all packages and subpackages
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python version
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",  # Who the package is for
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",  # Minimum Python version required
    install_requires=[
        "pytest>=7.4.0",  # List dependencies (e.g., pytest for tests)
        "coverage>=7.0.0",  # Add other libraries used by your code
    ],
    extras_require={
        "dev": ["flake8", "black", "isort"],  # Extra packages for development
    },
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/ScorestreamPy_lib/issues",
        "Documentation": "https://github.com/yourusername/ScorestreamPy_lib",
        "Source Code": "https://github.com/yourusername/ScorestreamPy_lib",
    },
)
