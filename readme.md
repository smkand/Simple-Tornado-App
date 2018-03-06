# Create a simple tornado application and deploy on Heroku

This repo will teach how to create a basic [tornado](http://www.tornadoweb.org/en/stable/) application from scratch and how to deploy it on [Heroku](https://www.heroku.com/).

## Prerequisites
```
Python  >= 2.7
Tornado >= 3.1.1
Heroku login credentials(free account option available)
Heroku CLI(Command Line Interface)
Docker(Only for app containerization)
```

## Installation 
1. Assuming all the prerequisites are installed, run the following command 
```
python main.py 

```
   Check the output on localhost:5000

2. Commands to login into Heroku CLI and to create heroku app 
```
heroku login 
[will ask for the login credentials]

heroku apps: create [filename]

```

3. To deploy this app on Heroku using git, run following command:
```
git push heroku master

```
Check the final output on the Heroku dashboard.
# Dockerize the tornado application 
Build the Docker image using this command:
```
docker build -t hello-tornado . 
```
Run the Docker container using this command:
```
docker run -d -p 5000:5000 hello-tornado
```
You can check for the final output on localhost:5000. 




