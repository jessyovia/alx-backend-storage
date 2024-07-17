# NoSQL Project

## Description
This project demonstrates basic operations with MongoDB, a NoSQL database. It covers:
- Listing databases
- Creating and using a database
- Inserting, querying, updating, and deleting documents
- Python integration with MongoDB using PyMongo

## Requirements
- MongoDB 4.2
- Python 3.7
- PyMongo 3.10

## Setup

### Install MongoDB 4.2
```sh
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start
