from setuptools import find_packages, setup

setup(
    name="QApplication",
    version="0.0.1",
    author="shree jagatap",
    author_email="shreedharjagatap2002@gmail.com",
    packages=find_packages(),
    install_requires=[]
)

#you have 2 option to install packages from pypi hub (using pip) and local packages in qa_env
#1) python setup.py install,,,using qa_env's python interpreter
#2) mention "-e ." ,,in requirements,txt ,,,as we did in mcq generator app,,,,,,,->-e means execution,,and . represent,,,in current working directory(which is 002_QA_System...)............whicih install the all locla packages whicih are in current working directoty,(folder which contains __init__.py file,,is considered as local package)..........,,pip install -r requirements.txt,,all global packages(llama-index,google-generativeai,...etc packages mentioned in requirements.txt) and locla packages are installed
    #ie; 2nd method-> when you run pip install -r requirements.txt,,it will automatically run setup.py which installs local packages and also installs all global packages mentioned in requirements.txt


#Read this to know more
#i have used 1st mehtod


#packages=find_packages() ->Find all locla packages,ie;user defined packages,,and install,,,so that we achieve modular coding,,,,ie;we can access data_ingestion.py functionality anywhere inside in our qa_env..
#mention packages that u want to install,,,,mention all files from requirements.txt,,,,thus no need to run requirements.txt,,,,,,,by running this file only,,we can install all packages mentioned here,,,and it will install all local packages (folder which contains __init_.py file,,is considered as local package)


#bottom right,,select 'qa_env',,bcz all our required pacakages are stored in this virtual env named qa_env,,,,,,,,,,thus ,,selcting python interpreter from this environment
#see,,,,,all these folders and files from 002_QA.... are not stored inside this qa_env,,,,,,,,,,,,,this qa_env just holds the packages(reuirements.txt and local packages(QAWithPDF)),,so thatwhen you run any python file using this qa_env environments python interpreter,,then python will access packages from this environment only,,which are required for running our files.........

#python setup.py install ...-> after running this in this (3.11.9('qa_env': conda)) environmanet,,,,,QAWithPDF name local package is instaled inside this qa_env,,,,(we have not mentioned any lib in install_requires=[] bcz we have already runned requirements.txt,,t ),,,,,,so just local packages are installed in qa_env
#thus after installing this packgae,,you see this QApplication with version 0.0.1 in your qa_env,this by importing this package in in any python file within qa_env,,you can access data_ingestion.py,embedding.py,model_api.py in it..
#As u see,,in embedding.py  "from QAWithPDF.data_ingestion import load_data", "from QAWithPDF.model_api import load_model",,,we have accessed it..

#ie; Thus QAWithPDF become our locla package or library..................

#numpy , pandas...etc are global packages,,,,bcz we have installed them through pypi hub of python using pip install command and stored in respective python environment
#ie;in qa_env i have installed python3.11.9 interpreter,,,,,,this  i if run pip install numpy inside this qa_env using this qa_env's python interpreter,,,package is installed and stored in this qa_env itself,not in base or not in global python env..etc

#see at bootom right,,,,,,,,which python interpreter is selected,,whcih indicates,,you are using which environment for executing files..thus,,if file require any package/lib to run,,then from this qa_env only package is used for executing the files


#After executing python setup.py install,,,you will notice new folder and files are cteated in current working directory (002_QA_system_Using_Llama_Index_And_Gemini)
#build , dist , QApplication.egg-info,which contains author info,,that whoc created this package , 