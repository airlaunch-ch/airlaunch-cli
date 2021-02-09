#!/usr/bin/env python

import yaml
import os
import os.path
import subprocess
import sqlite3
import sys

if len(sys.argv) != 3:
    print("need to provide airflow_home path as first argument, connections file path as second argument.")
    exit(0)

airflow_home = sys.argv[1]
connections_file = sys.argv[2]

def get_value_or_none(key, dict):
    try:
        return dict[key]
    except KeyError:
        return None

def append_if_not_none(argument, value, command):
    if value is not None:
        command.append(argument)
        command.append(str(value))

def drop_all_connections():
    conn = sqlite3.connect('{}/airflow.db'.format(airflow_home))
    conn.execute("DELETE FROM connection")
    conn.commit()

def load_configured_connections():
    with open(connections_file, 'r') as stream:
        try:
            print("loading configured connections")
            connections = yaml.safe_load(stream)
            if connections is not None:
                for conn_id, conn in connections.items():
                    command = ["airflow", "connections", "add", conn_id]
                    
                    conn_type = get_value_or_none("conn_type", conn)
                    append_if_not_none("--conn-type",conn_type, command)

                    extra = get_value_or_none("extra", conn)
                    append_if_not_none("--conn-extra",extra, command)

                    host = get_value_or_none("host", conn)
                    append_if_not_none("--conn-host",host, command)

                    login = get_value_or_none("login", conn)
                    append_if_not_none("--conn-login",login, command)

                    password = get_value_or_none("password", conn)
                    append_if_not_none("--conn-password",password, command)

                    port = get_value_or_none("port", conn)
                    append_if_not_none("--conn-port",port, command)

                    schema = get_value_or_none("schema", conn)
                    append_if_not_none("--conn-schema",schema, command)

                    description = get_value_or_none("description", conn)
                    append_if_not_none("--conn-description",description, command)
                    
                    uri = get_value_or_none("uri", conn)
                    append_if_not_none("--conn-uri",uri, command)
                    process = subprocess.Popen(command, stdout=subprocess.PIPE)
                    output, error = process.communicate()
                    if error != None:
                        print("error loading connection {}".format(conn_id))
                    print(output.decode("utf-8").strip())
        except yaml.YAMLError as exc:
            print(exc)


if os.path.isfile(connections_file):
    drop_all_connections()
    load_configured_connections()


