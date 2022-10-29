from setuptools import setup

with open("README.md",'r') as f:
  LNG=f.read()

setup(name="Giturlgetter",
version="0.4",
description="Command Line to Extract the git url",
author="Prathamesh Dhande",
author_email='prathameshdhande534@gmail.com',
long_description=LNG,
long_description_content_type='text/markdown',
packages=['command_line'],
install_requires=['clipboard','PyGithub','requests','pyfiglet','python-dotenv'],
entry_points={
    'console_scripts': [
            'giturl=command_line.__main__:run',
        ]
},
classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers   # Again, pick a license   #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ]

)