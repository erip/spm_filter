from setuptools import setup, find_packages

long_description = open("README.md", encoding="utf-8").read()

setup(
    name="spm_filter",
    version="0.1.0",
    description="A CLI for filtering segments which don't meet length criteria after SentencePiece encoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erip/spm_filter",
    author="Elijah Rippeth",
    author_email="elijah.rippeth@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    python_requires=">=3.7, <4",
    entry_points={
        "console_scripts": [
            "spm-filter=spm_filter.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/erip/spm_filter/issues",
        "Source": "https://github.com/erip/spm_filter",
    },
)
