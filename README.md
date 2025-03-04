# Healthcare RAG with MIMIC-III

This repository demonstrates Retrieval-Augmented Generation (RAG) techniques applied to healthcare data using the MIMIC-III database.

## Project Overview

This project implements a RAG system that can answer questions about hospital admission data by:
- Querying MIMIC-III admission records
- Converting text to embeddings using sentence transformers
- Building a FAISS vector index for efficient retrieval
- Using prompt engineering to improve answer generation with OpenAI models

**Please note:**
* This pipeline is not comprehensive or production-ready. It intentionally omits advanced error handling, extensive logging, modularization, and configurable parameters.
* Future work (e.g., an upcoming RAG pipeline with clinical notes) will incorporate these enhancements along with more robust preprocessing, healthcare-specific embedding models, and improved evaluation metrics.


## Key Features

- Simple but functional RAG pipeline for healthcare data
- Comparison of basic vs. enhanced prompt engineering approaches
- Demonstration of date/time reasoning in medical context
- Framework for extending to more complex clinical notes

## Getting Started

### Prerequisites

1. MIMIC-III access through PhysioNet
2. Google Cloud account with BigQuery access
3. OpenAI API key

### Installation


1. Clone this repository
   ```bash
    git clone https://github.com/kulsoom-abdullah/mimic-simple-rag.git
    cd mimic-simple-rag
```
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key: like OPENAI_API_KEY="key-here"

### Important Setup Instructions

Before running the notebook, please ensure the following:

1. **Google Cloud Authentication:**  
   Authenticate your Google Cloud account for BigQuery access by running:
   ```bash
   gcloud auth application-default login
```
Alternatively, set up a service account with the required permissions and define the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to your JSON key file. For more details, refer to the Google Cloud Authentication Guide.

2. Notebook Execution:
Open the Jupyter Notebook (mimic_simple_rag.ipynb) and run the cells step by step to verify that everything executes without errors.

3. Dependencies and First-Run Experience:
Run the following command to install all required dependencies:

   ```bash
pip install -r requirements.txt
```
Note that some large models (e.g., the sentence-transformers model) will be downloaded on first use. This may take a few minutes during the initial run.

## Usage

The main notebook demonstrates the complete pipeline:

```python
# Set your Google Cloud project
os.environ["GOOGLE_CLOUD_PROJECT"] = "your-project-name"

```

## RAG Pipeline Architecture

![Healthcare RAG Pipeline Architecture](images/rag_pipeline_architecture.png)

The implementation follows a standard RAG pattern with healthcare-specific components:
1. Data is extracted from MIMIC-III patient admission records
2. Text is preprocessed and chunked to maintain clinical context
3. Embeddings are generated using Sentence Transformers
4. User queries are similarly embedded and compared against the index
5. Retrieved contexts are combined with enhanced prompting tailored for medical data
   
## Limitations

- This is a minimal example using only admission data
- Limited to a small number of records for demonstration
- Does not include more complex healthcare-specific preprocessing
- Uses general-purpose embeddings rather than clinical embeddings


## Potential Future Work

The next phase will extend this approach to clinical notes in MIMIC-III, implementing:
- Advanced chunking strategies for longer medical texts
- Healthcare-specific embedding models
- Multi-chunk retrieval and context management
- Named entity recognition for medical terms

## License

This project is licensed under the MIT License - see the LICENSE file for details.
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![RAG](https://img.shields.io/badge/RAG-Pipeline-orange.svg)

## Acknowledgments

- [MIMIC-III Clinical Database](https://physionet.org/content/mimiciii/1.4/)
- [PhysioNet](https://physionet.org/) for hosting the data
- [LangChain](https://github.com/langchain-ai/langchain) for RAG components
- [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers) for embeddings
- [FAISS](https://github.com/facebookresearch/faiss) for vector indexing
