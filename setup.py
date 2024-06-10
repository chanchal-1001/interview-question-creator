# to consider all the folder a package we use setup
# To download in local folder

from setuptools import find_packages, setup
#/ineuron_Seven_project/interview-question-creator
#https://github.com/entbappy/Interview-Question-Creator/blob/main/src/helper.py

#https://whimsical.com/JAhkxhoPHGXa7B1DdPN55

#https://github.com/entbappy/Deploy-Streamlit-app-on-EC2-instance

#https://askubuntu.com/questions/1465218/pip-error-on-ubuntu-externally-managed-environment-%C3%97-this-environment-is-extern

setup(
    name= "Generative AI Project",
    version= "0.0.0",
    author="Chanchal",
    author_email="entbuppy73@gmail.com",
    packages=find_packages(),#looks for __init__ to setup in local sy
    install_requries = []
)

# sudo apt update
# sudo apt-get update
# sudo apt upgrade -y
# sudo apt install git curl unzip tar make sudo vim wget -y
# git clone "Your-repository"
# touch .env to generate new file
# sudo apt install python3-pip
# sudo apt install python3-venv
# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install -r requirements.txt
# #Temporary running
# python3 -m streamlit run app.py
# #Permanent running
# nohup python3 -m streamlit run app.py
# Note: Streamlit runs on this port: 8501