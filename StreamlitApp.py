import streamlit as st #global package
from QAWithPDF.data_ingestion import load_data #QAWithPDF is a local package
from QAWithPDF.embedding import download_gemini_embedding #local package
from QAWithPDF.model_api import load_model #load_model() is a function present inside model_api.py file,,and which is present inside QAWithPDF folder or directory............and bcz QAWithPDF contains __init__.py file,,it become local package/library,,,,,,and by executing setup.py file using python interpreter from qa_env,,we have downloaded /installed this local package in our qa_env,thus it is accessible through qa_env
import os
#Local packgae -> user has defined and installed in his environment
#global package -> which are developed by develope and uploaded on pypi hub of python,,,,,,,so we can install it using python interpreters pip command..........ex-> all packages you used by downloading them through pip command ie;numpy,pandas,math,scikit-learn,bs4,flask,seaborn..etc

    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")


    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data(doc)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                

from google.auth import default

if __name__=="__main__":
    
    main()
