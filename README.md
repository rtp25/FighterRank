# FighterRank

FighterRank is a CRUD web application that ranks the top ten MMA fighters of four different weight classes in the UFC fighting promotion. The unique ranking system uses an algorithm that involves six metrics of each fighter: win %, KO win %, submission win %, decision win %, striking accuracy % and grappling accuracy %. 


## Dependencies

You will need to install the following dependencies before you get started.

1. Install [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) 
2. Install [Python 3.x](https://www.python.org/downloads/)
3. Install Flask and set up your virutal environment (venv) using the package manager [pip](https://pip.pypa.io/en/stable/).

```
pip install Flask
```
Here is a link that explaines how to set up Flask and a venv in more detail:
(https://flask.palletsprojects.com/en/1.1.x/installation/) 


## Running the program

Here are some notes to consider before the run the program.

1. Make sure you are the FighterRank/app directory. 

```
cd FighterRank\app
```

2. Make sure you are connected to the database and that the MySQL Server is running.
3. Set your environment variables.
    - set FLASK_ENV = development
    - set FLASK_APP = main.py
  
4. Run the program with the following command:
```
flask run
```
5. Open your browser and type the following in the address bar the see FighterRank web application in action.
```
http://localhost:8080
```


## Upcoming Changes

1. The environment variables will be configured automatically instead of manually. 
2. FighterRank still needs to fix the PUT requests for the fighters. 
3. The front-end can be updated to be more aesthetic.

## Authors

* **Rogelio Paniagua** 

