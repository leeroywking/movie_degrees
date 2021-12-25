# Six degrees of Lee-Roys Bacon

## Credits:
I used this dataset from kaggle
https://www.kaggle.com/gorochu/complete-imdb-movies-dataset

## Setup instructions
After cloning this repo down you will need to build the database for the program this is done by running the command 
`python3 build_actor_links.py`


## Run the application
this was written using the standard libraries for Python3 so you should be able to run the program from your terminal by typing 
`python3 degree_finder.py`


## Alternate application
If you don't want to store 300mb in a file or you have a slow hard disk this may be a better solution for you but startup time for the program can be slow.
`python3 in_mem_degree_finder.py`


(Actually it seems pretty good it might just be better overall)