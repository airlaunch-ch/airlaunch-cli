# Airlaunch Local Airflow Development Environment
This is a local Airflow development enviornment.
It bootstraps a fully functional Airflow installation in a python venv and offers convenience functions to manage its configuration.
It leaves your computer unchanged otherwise. 

# Getting started

1. Install dependencies
In order for the environemnt to work, you need:
   - Python 3.6+
   - Python virtualenv (```pip install virtualenv```)


2. clone this repo: ```git clone https://github.com/airlaunch-ch/airlaunch-cli.git && cd airlaunch-cli```
3. Install the script to a location in your path: ```chmod +x ./air && sudo cp ./air /usr/local/bin/```

5. Go to your dags folder and initialize the environment: 
   
   ```air init```

6. Start airflow:
   
   ```air start```

Thats's it! Airflow is now available on localhost:8080

# Testing DAGs
You can easlily run DAGs without needing to start the webserver. 
Simply run 

```air test [dag_id] ([execution_date])```

This will run the dag in question. The execution date is optional. If you do not provide it, the current date will be used. 

# Interact with the Airflow instance
You can run any airflow command using the command passthrough functionality:

```air pass [airflow command]``` 

This command temporarliy sets the environment variables and activates the venv and then passes the command to airflow unchanged. 

You can run any airflow command using the command passthrough. 

# Configuration
There are three relevant configuration files: 

**.env**
The main user facing configuration file. A default config file will be generated on init. 
The default configuration should work fine for most people. Check inside the file for documentation of the ways you can customize your environment. 

**connections.yaml**
A yaml file holding airflow connections (i.e. your database credentials). 
Check the official [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#exporting-connections-from-the-cli) to learn more about the format that is expected. 
You can also load all connections in the Airflow web interface and then generate this file with 

```air export```

**requirements.txt**
The pip requirements file holding additional packages to be installed. Put your python dependencies there and run

```air install-requirements```

You can configure where airflow looks for this file in the .env file. By default it is located in the DAG folder. 

# Contributing

If you found a bug or want to improve this package, feel free to open a pull request. 
