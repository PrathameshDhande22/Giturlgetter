from setuptools import setup

with open("README.md",'r',encoding="UTF-8") as f:
  LNG=f.read()

setup(name="Giturlgetter",
version="1.0.5",
description="Command Line to Extract the git url",
author="Prathamesh Dhande",
author_email='prathameshdhande534@gmail.com',
long_description=LNG,
long_description_content_type='text/markdown',
packages=['command_line'],
install_requires=['PyGithub','requests','pyfiglet','python-dotenv'],
entry_points={
    'console_scripts': [
            'giturl=command_line.__main__:run',
        ]
},
url="https://github.com/PrathameshDhande22/Giturlgetter",
keywords=["git","git url","github api","url","git bash","clone url"],
classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers', 
    'Environment :: Console',  
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',   # Define that your audience are developers   # Again, pick a license   #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ]

)