# NLTK Text Processing Pipeline

A Jupyter notebook demonstrating a custom text-processing pipeline built with **NLTK** (Natural Language Toolkit). It covers three core NLP tasks — custom tokenization, POS-tag-aware lemmatization, and sentence segmentation — applied to a sample passage containing dates, emails, emojis, and hashtags.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Notes / Limitations](#notes--limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Custom Regex Tokenization**: A hand-crafted regex pattern (`nltk.regexp_tokenize`) that correctly handles:
  - Gregorian dates (`9/15/2005`)
  - Iranian calendar dates (`1384/6/24`)
  - Email addresses (`roozbehseyednozadi@gmail.com`)
  - Contractions (`don't`)
  - Hashtags (`#HALAMadrid`)
  - Emojis and other non-ASCII characters (`😂`)
  - Punctuation as separate tokens
- **POS-Aware Lemmatization**: Uses `nltk.pos_tag` combined with `WordNetLemmatizer` to lemmatize each token according to its part of speech (noun, verb, adjective, adverb), rather than defaulting to a single POS.
- **Sentence Segmentation**: Splits the raw passage into sentences using `sent_tokenize`.

## Prerequisites

- Python 3.12+
- Jupyter Notebook / JupyterLab

## Installation

1. Clone or download this repository.
2. Install the required packages:

   ```bash
   pip install nltk 
   ```

3. Download the necessary NLTK data packages:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('averaged_perceptron_tagger_eng')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   ```

## Usage

Launch the notebook:

```bash
jupyter notebook NLTK.ipynb
```

Run the cells in order. The notebook is organized into three parts:

| Part | Section | Description |
|------|---------|-------------|
| 1 | Tokenization | Tokenizes the sample passage using a custom regex pattern |
| 2 | Lemmatization | Tags each token with its part of speech and lemmatizes accordingly |
| 3 | Sentence Segmentation | Splits the passage into individual sentences |

### Example

**Input passage** (excerpt):
```
Hi, my name is Roozbeh Seyednozadi and I was born in 9/15/2005...
```

**Tokenized output** (excerpt):
```python
['Hi', ',', 'my', 'name', 'is', 'Roozbeh', 'Seyednozadi', ..., '9/15/2005', ...]
```

**Lemmatized output** (excerpt):
```python
['Hi', ',', 'my', 'name', 'be', 'Roozbeh', 'Seyednozadi', ..., 'bear', ...]
```

**Segmented sentences** (excerpt):
```python
['Hi , my name is Roozbeh Seyednozadi and I was born in 9/15/2005...',
 'My heigh is 184cm and my weight is about 83kg.',
 ...]
```

## Project Structure

```
.
├── NLTK.ipynb   # Main notebook: tokenization, lemmatization, sentence segmentation
└── README.md
```

## Dependencies

- [nltk](https://www.nltk.org/) — core NLP toolkit (tokenization, POS tagging, WordNet lemmatization, sentence segmentation)

## Notes / Limitations

- The regex tokenizer is tailored to the sample passage's format (e.g., date patterns, email format) and may need adjustment for other texts.
- Lemmatization quality depends on the accuracy of the POS tagger; ambiguous words may lemmatize imperfectly (e.g., `"is"` → `"be"`, `"was born"` → `"bear"`, following WordNet's verb lemmas).

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Make your changes to the notebook (e.g., extend the regex pattern, add new NLP tasks, improve lemmatization coverage).
4. Ensure the notebook runs cleanly from top to bottom before submitting.
5. Commit your changes with a clear message (`git commit -m "Add X"`).
6. Push to your branch and open a Pull Request describing the change.

You can also reach out via email at rseyednozadi@gmail.com.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
