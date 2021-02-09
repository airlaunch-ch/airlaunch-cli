# Airlaunch Local Airflow Development Environment
This is a local Airflow development enviornment.
It bootstraps fully functional Airflow installation in a python venv and offers convenience functions to manage its configuration.
It leaves your computer unchanged otherwise. 
# Getting started

1. Install dependencies
In order for the environemnt to work, you need:

- Python 3.6+
- Python virtualenv (```pip install virtualenv```)
- [Airflow system dependencies](https://airflow.apache.org/docs/apache-airflow/stable/installation.html#system-dependencies)

2. Initialize environment: 
   
   ```./air init```

3. Start airflow:
   
   ```./air start```

Thats's it! Airflow is now available on localhost:8080

# Testing DAGs
To test dags without needing to start the web server, you can use the airflow command line interface. 
You can run airflow commands using the command passthrough functionality:

```./air pass [airflow command]``` 

This command temporarliy sets the environment variables and activates the venv and then passes the command to airflow unchanged. 

To test airflow dags and tasks indiviually, simply run

```./air pass dags test [dag_id] [exechution_time]```

You can run any airflow command using the command passthrough. 
# Configuration

There are three relevant configuration files: 

**.env**
The main user facing configuration file. 
The default configuration should work fine for most people. Check inside the file for documentation of the ways you can customize your environment. 

**connections.yaml**
A yaml file holding airflow connections (i.e. your database credentials). 
Check the official [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#exporting-connections-from-the-cli) to learn more about the format that is expected. 
You can also load all connections in the Airflow web interface and then generate this file with 

```./air export```

**requirements.txt**
The pip requirements file holding additional packages to be installed. Put your python dependencies there and run

```./air install-requirements```

You can configure where airflow looks for this file in the .env file. By default it is located in the DAG folder. 
