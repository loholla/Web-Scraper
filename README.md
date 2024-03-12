# Welcome to my Web Scraper 
## This project was made for my CS325 class, but it is a program that will take the link from a news article and output the raw text without any HTML tags. 

### Before doing anything else:
Make sure you download the .yaml file and run.py, along with all of the other files.

### How to set up the environment to run the program:
First, make sure you have miniconda installed and running. Once the terminal for miniconda is open, you will need to run the command "conda env create -f requirement.yaml" or, if you want to rename the environment, "conda env create -n (Your_Environment_Name) -f requirement.yaml".

Once the conda environment is created, run "conda activate (environment_name)". With the default name, the command will be "conda activate CS325"

Now that the environment is open, you will have to use the command "cd" to get into the folder containing the run.py file. In this same file, you can make (or add) the list of articles in a .txt file. You can also indicate an absolute path if you have a file you want to process that isn't in the same directory as run.py

In the .txt file, paste the URLs of the news articles you want to scrape. -Note, this will only work with CNN news articles

### Running the program:
To run the program, in miniconda type "python run.py (file_path or file_name)", and then the program will run.

After you hit enter, the program will output a raw data file and a processed data file for each article.
