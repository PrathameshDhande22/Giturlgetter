# GIT URL GETTER

![](https://img.shields.io/badge/Python-3.8_|_3.9_|_3.10-blue?logo=python&style=flat-square&logoColor=white)&nbsp;
![](https://img.shields.io/badge/Github-API-red?logo=github&style=flat-square&logoColor=white)
&nbsp; ![GitHub repo size](https://img.shields.io/github/repo-size/prathameshdhande22/Giturlgetter?color=brown&logo=github&style=flat-square)
&nbsp; ![PyPI - Downloads](https://img.shields.io/pypi/dd/giturlgetter?color=blue&logo=pypi&logoColor=white)
&nbsp; ![PyPI - License](https://img.shields.io/pypi/l/giturlgetter?color=success&logo=pypi&logoColor=white)
&nbsp; ![GitHub Repo stars](https://img.shields.io/github/stars/prathameshdhande22/giturlgetter?style=social)
</br>

![](https://img.shields.io/badge/MADE_WITH_%20-Python-f02b79%20?style=for-the-badge&logo=python&labelColor=Ff00d8&color=Ff0087&logoColor=white)


Github Has Released the **Github CLI (Command Line Interface)** using we can create the Github Repo in terminal only without Browsing the Browser.
</br> </br>
But in Github CLI you cannot get the git url so using **Giturlgetter** Python Library you can get the git url using very simple steps.</br>

You Either Use the Python Library or the GUI which is in Another branch.</br>

# Works For ![](https://ucarecdn.com/51bca072-f640-42c0-b316-f0c0d742779c/-/preview/30x30/) 10/11/7 Only.

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
pip install .\Giturlgetter-0.5-py3-none-any.whl
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

## Usage:
<img src="./Images/giturlgetter.gif">

## Commands:
1. `giturl login` -> To Login through Github with Activation Code.
2. `giturl --version` -> To Get the Version Info.
3. `giturl -h` -> To get help for any any command you can use `command -h`.
4. `giturl logout` -> To Logout from the device.
5. `giturl list --default` -> To list the user Repository Name and ID.
6. `giturl list` -> Prompts the user to enter the username of the user to list the repositories Name and ID.
7. `giturl repo` -> Prompts the user to enter the Repository name or ID to get the clone url, ssh url, html url, git url.
8. `giturl repo -id,--id` or `giturl -n,--name` -> To get the urls.
9. `giturl details` -> Prompts the User to enter the username and fetches entered username details.

## Upcomming Version v1.0.10:
More devices will supported

## Author : Prathamesh Dhande