# Welcome to my Web Scraper 
## This project was made for my CS325 class, but it is a program that will take the link from a news article and output the raw text without any HTML tags. 

### Before doing anything else:
Make sure you have downloaded at least the requirement.yaml and the scraper.py. If you are wanting to run the example list, you can also download articles.txt.

### How to set up the environment to run the program:
First, make sure you have miniconda installed and running. Once the terminal for miniconda is open, you will need to run the command "conda env create -f requirement.yaml" or, if you want to rename the environment, "conda env create -n (Your_Environment_Name) -f requirement.yaml".

Once the conda environment is created, run "conda activate (environment_name)". With the default name, the command will be "conda activate CS325-Web_Scraping-loholla"

Now that the environment is open, you will have to use the command "cd" to get into the folder containing the scraper.py file. In this same file, you should make (or add) the list of articles in a .txt file.

In the .txt file, paste the URLs of the news articles you want to scrape. -Note, this will only work with CNN news articles

### Running the program:
To run the program, in miniconda type "python scraper.py", and then the program will prompt you to input a file destination. If you use my example file, the input should be "articles.txt" (Do not put in the quotation marks, or it won't accept it).

After you hit enter, the program will output a file for each article with all of the important text from each article.
