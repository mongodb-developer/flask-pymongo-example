# flask-pymongo-example

```
$$$$$$$$\ $$\                     $$\               $$$$$$$\            $$\      $$\                                               
$$  _____|$$ |                    $$ |              $$  __$$\           $$$\    $$$ |                                              
$$ |      $$ | $$$$$$\   $$$$$$$\ $$ |  $$\         $$ |  $$ |$$\   $$\ $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        
$$$$$\    $$ | \____$$\ $$  _____|$$ | $$  |$$$$$$\ $$$$$$$  |$$ |  $$ |$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       
$$  __|   $$ | $$$$$$$ |\$$$$$$\  $$$$$$  / \______|$$  ____/ $$ |  $$ |$$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |      
$$ |      $$ |$$  __$$ | \____$$\ $$  _$$<          $$ |      $$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      
$$ |      $$ |\$$$$$$$ |$$$$$$$  |$$ | \$$\         $$ |      \$$$$$$$ |$$ | \_/ $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$  |      
\__|      \__| \_______|\_______/ \__|  \__|        \__|       \____$$ |\__|     \__| \______/ \__|  \__| \____$$ | \______/       
                                                              $$\   $$ |                                 $$\   $$ |                
                                                              \$$$$$$  |                                 \$$$$$$  |                
                                                               \______/                                   \______/                 
       $$$\                                                                                                                        
      $$ $$\                                                                                                                       
      \$$$\ |                                                                                                                      
      $$\$$\$$\                                                                                                                    
      $$ \$$ __|                                                                                                                   
      $$ |\$$\                                                                                                                     
       $$$$ $$\                                                                                                                    
       \____\__|                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
$$\      $$\                                         $$$$$$$\  $$$$$$$\         $$$$$$\    $$\     $$\                             
$$$\    $$$ |                                        $$  __$$\ $$  __$$\       $$  __$$\   $$ |    $$ |                            
$$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$ |$$ |  $$ |      $$ /  $$ |$$$$$$\   $$ | $$$$$$\   $$$$$$$\         
$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$$$$$$\ |      $$$$$$$$ |\_$$  _|  $$ | \____$$\ $$  _____|        
$$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |$$  __$$\       $$  __$$ |  $$ |    $$ | $$$$$$$ |\$$$$$$\          
$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |  $$ |$$\ $$ |$$  __$$ | \____$$\         
$$ | \_/ $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |$$$$$$$  |      $$ |  $$ |  \$$$$  |$$ |\$$$$$$$ |$$$$$$$  |        
\__|     \__| \______/ \__|  \__| \____$$ | \______/ \_______/ \_______/       \__|  \__|   \____/ \__| \_______|\_______/         
                                 $$\   $$ |                                                                                        
                                 \$$$$$$  |                                                                                        
                                  \______/                                                                                         
```
## Introduction

Implementation of flask and pymongo using mflix sample data set and mflix python UI

This is a short guide on how to integrated MongoDB Atlas to Flask applications using Flask-PyMongo wrapper and pymongo driver.

## Project Structure

The `mflix` directory holds the application logic.

- `db.py` Where all database CRUD patterns are exposed as functions.
- `api/movies.py`  Where the web api is exposed to the UI

The main directory holds the following files:
- `run.py` Where the Flask application is initialize and the config is loaded
- `sample_ini` Where the connection URI to MongoDB Atlas is configured
- `requirments.txt` Where the dependencies this project needs to run are located.

## How to set-up

Clone the repository.
```
git clone git@github.com:mongodb-developer/flask-pymongo-example.git
```

Start a python virtual env:
```
# navigate to the flask-pymongo-example directory
cd flask-pymongo-example

# create the virtual environment for MFlix
python3 -m venv mflix-venv

# activate the virtual environment
source mflix_venv/bin/activate
```

Install dependencies
```
python3 -m pip install -r requirements.txt
```

Rename the `sample_ini` to `.ini`.
```
mv sample_ini sample.ini
```

[Get your Atlas cluster](https://docs.atlas.mongodb.com/getting-started/) with [sample data](https://docs.atlas.mongodb.com/sample-data/) set [connection string](https://docs.atlas.mongodb.com/connect-to-cluster/) and place in `DB_URI` parameter under `.ini`

Make sure you have IP in the Atlas [access list](https://docs.atlas.mongodb.com/security/add-ip-address-to-list/) and username/password of your Atlas user correctly specified.

## Start the application

```
python ./run.py
```

Open your browser on http://localhost:5000

## Disclaimer 

Use at your own risk; not a supported MongoDB product
