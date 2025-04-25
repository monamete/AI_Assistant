from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:

       requirements=file_obj.readlines()
       [req.replace("\n","") for req in requirements] 

       if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
    return requirements
       
    
           
setup(
    name="AI_ASSISTANT",
    version="3.12.10",
    author="Monika",
    author_email="monikasatpute23@gmail.com",
    packages=find_packages(),
    install_requires=[
    "streamlit",
    "scikit-learn",
    "pandas",
    "faiss-cpu",
    "joblib",
    "openai",
    "numpy",
    "GitPython",
    "faiss-cpu"
    ""

    
]



)