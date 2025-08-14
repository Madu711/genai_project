from setuptools import setup, find_packages

setup(
    name="mcq_generator",
    version="0.0.1",
    author = "Raghavendra",
    author_email="raghavendramadu@gmail.com",
    description="A package for generating multiple-choice questions",
    install_requires=["openai", "langchain", "streamlit", "PyPDF2", "python-dotenv"],
    packages=find_packages(),

)