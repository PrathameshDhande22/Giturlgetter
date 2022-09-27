# GIT URL GETTER

![](https://img.shields.io/badge/Python-3.6_|_3.7_|_3.8_|_3.9_|_3.10-blue?logo=python&style=flat-square&logoColor=white)&nbsp;
![](https://img.shields.io/badge/Github-API-red?logo=github&style=flat-square&logoColor=white)</br>


<center>

![](https://img.shields.io/badge/MADE_WITH_%20-Python-f02b79%20?style=for-the-badge&logo=python&labelColor=Ff00d8&color=Ff0087&logoColor=white)
</center>

Github Has Released the **Github CLI (Command Line Interface)** using we can create the Github Repo in terminal only without Browsing the Browser.
</br> </br>
But in Github CLI you cannot get the git url so using **Giturlgetter** Python Library you can get the git url using very simple steps.</br>

You Either Use the Python Library or the GUI which is in Another branch.</br>

## Installation :
Install the Library from the command pip :
```
pip install Giturlgetter
```
Or Install using the git repository
</br>

Clone the Repository
```
git clone https://github.com/PrathameshDhande22/Giturlgetter.git
cd Giturlgetter
```

Install Using the setup.py
```
cd .\dist\
pip install .\Giturlgetter-0.3-py3-none-any.whl
```
You Have Successfully Installed the Library.
</br>

## Automate Your Github Work :

If You are Tired of Creating the Github Repository in browser and then copying the git url so it becomes the Complicated work.
</br>

Download the GitHub CLI from <a href="https://github.com/cli/cli/releases/"> Here.</a></br>
Before Installing the GitHub CLI please install the git from <a href="https://git-scm.com/downloads"> Here</a></br>
Read the <a href="https://cli.github.com/manual/index">Manual</a> for GitHub CLI</br>
Python >=3.6 Should be install in you System.
</br>

**Create the GitHub Repo without Visiting the Browser**:</br>

- To Create The GitHub Repo.</br>
Use Command : 
```
gh repo create
```
Select the Options.</br>

***Note*** : Don't select the Clone Repo or not create any file.</br>

- Initialise the git using.</br>

```
git init
git add .
git commit -m "First Commit"
```

* After Installing the Giturlgetter library.</br>
Run the Following command :
```
giturl
```
This will ask to Enter the Github API Token, So Generate The Token From [Here](https://www.google.com/url?sa=t&source=web&rct=j&url=https://github.com/settings/tokens&ved=2ahUKEwiFi6my3Kf6AhXRDKYKHaWKCAsQFnoECBcQAQ&usg=AOvVaw1aAJGUMBmPGH7oCTvgDvQv)</br>
Let's Go.</br>
Select the Option **1** To get the Git Url -> Enter the Github Username of which you want the URL -> After Generating the List of Repos -> Enter the Index Number of the Repository name -> After the Git URL will be copied to Your clipboard.


## Author : Prathamesh Dhande