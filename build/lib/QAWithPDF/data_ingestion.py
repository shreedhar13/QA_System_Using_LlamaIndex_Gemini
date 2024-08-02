from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception #in exception.py file this Customexception Class we have created,,,so this code will access it..See how to create custom modules/library,,bcz to perform modular coding and to access these module in diiff-diff files,,we have to create custom modules,,,,,like we created for exception...and this custom module is called local packages/module/librabry
from logger import logging


def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)