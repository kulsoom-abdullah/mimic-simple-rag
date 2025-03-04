# Healthcare RAG Pipeline with Synthetic Data

This folder contains a simplified version of the RAG pipeline that uses **synthetic hospital admission data**. It is designed for users who do not have access to the MIMIC-III dataset or BigQuery but still want to experiment with RAG systems.

## Getting Started

### Prerequisites
1. Python 3.9+
2. OpenAI API key (stored in a `.env` file)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/kulsoom-abdullah/mimic-simple-rag.git
   cd mimic-simple-rag/synthetic_data_version
    ```
2. Install dependencies:

   ```bash
    pip install -r ../requirements.txt
    ```
3. Set up the .env file:
Create a .env file in the root directory and add your OpenAI API key
   ```bash
    echo 'OPENAI_API_KEY="your-api-key-here"' > .env
    ```


### Usage
1. Generate Synthetic Data:
Run the admissions_data_generator.py script to create a CSV file (`synthetic_admissions.csv`):

   ```bash
    python admissions_data_generator.py
    ```
2. Run the Notebook:
Open the `mimic_simple_rag_synthetic.ipynb` notebook and follow the instructions to load the synthetic data and run the pipeline.

## Limitations
- The synthetic data is randomly generated and does not reflect real-world patterns.
- This version does not include advanced features like prompt engineering or evaluation metrics.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for RAG components
- [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers) for embeddings
- [FAISS](https://github.com/facebookresearch/faiss) for vector indexing
- [OpenAI](https://openai.com/) for providing the GPT model used in this project.
