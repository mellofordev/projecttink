# Tapai Extractor (for Training Set PDF -> Clean TXT) Python Script

This repository contains a PDF extractor for the training set of the Tapai project. The extractor allows you to convert PDF files into corresponding text files for further processing and analysis.

## How to Use

Follow the steps below to set up and run the PDF extractor:

### Prerequisites

1\. Install Python: Make sure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

2\. Install pip: Pip is the package installer for Python. If you don't have it installed, follow the instructions on the official pip website: [pip.pypa.io](https://pip.pypa.io/en/stable/installing/).

### Setup

1\. Clone the repository: Clone this repository to your local machine using the following command:

```bash

git clone https://github.com/mellofordev/tapai_extractor.git

```

2\. Install dependencies: Navigate to the cloned repository's directory and install the required packages using the `requirements.txt` file:

```bash

cd tapai_extractor

pip install -r requirements.txt

```

3\. Create and activate a virtual environment: To ensure a clean and isolated environment, it is recommended to use a virtual environment. Run the following commands to create and activate a virtual environment:

```bash

python -m venv venv         # Create virtual environment

source venv/Scripts/activate  # Activate the virtual environment on Windows, use "venv/bin/activate" for macOS/Linux

```

### API Key Setup

1\. Create a `.env` file: In the working directory, create a file named `.env`.

2\. Add the API Key: Inside the `.env` file, add the following line and replace `provided_key` with your actual API key:

```plaintext

API_KEY=provided_key

```

Note: Replace `provided_key` with the actual API key provided to you by mello, inc.

### Extract PDFs

1\. Place PDF files: Place all the PDF files you want to extract inside the working directory.

2\. Sample PDF: There is a `sample.pdf` file included in the repository for testing purposes.

3\. Run the extractor: To begin the extraction process, run the following command:

```bash

python extractor.py

```

### Output

Upon successful execution, the extractor will convert the PDF files into corresponding text files. The output text files will be created with the same names as the source PDF files, but with the extension changed to `.txt` and prefixed with "cleaned_". For example, if you had a PDF named `document.pdf`, the extracted text file will be named `cleaned_document.txt`.

Make sure to check the working directory for the extracted text files (`*.txt`) once the extraction process is complete.