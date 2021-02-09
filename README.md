# Airlaunch Local Development Environment
This is a local Airflow development enviornment.
It bootstraps fully functional Airflow installation on your local computer and offers convenience functions to manage its configuration

# Configuration

There are three relevant configuration files: 

**.env**
The main user facing configuration file. 
The default configuration should work fine for most people. Check inside the file for documentation of the ways you can customize your environment. 

**connections.yaml**
A yaml file holding airflow connections (i.e. your database credentials). 
Check the official [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#exporting-connections-from-the-cli] to learn more about the format that is expected. 
