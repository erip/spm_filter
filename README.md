# spm-filter

A unix-like utility for filtering raw sentences depending on their post-encoded lengths.

## Installation

```sh
git clone git@github.com:erip/spm_filter.git
cd spm_filter
pip install -e .
```

## Usage

```sh
# Read from stdin by default
cat sents.txt | spm-filter -m /path/to/sentencepiece.model --max-len 256 > filtered.txt
# Or read from a file
spm-filter -i sents.txt -m /path/to/sentencepiece.model --max-len 256 > filtered2.txt
```

## Authors
- [Elijah Rippeth](mailto:elijah.rippeth@gmail.com)
