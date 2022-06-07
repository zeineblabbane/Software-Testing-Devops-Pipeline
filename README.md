# Software-Testing-Devops-Pipeline
This project is an application that manages users, with basic CRUD features. We can add, edit or delete user. 
We will apply all different test levels as well as create a CI/CD pipeline for the project.

## Project Prerequisites
Run below command to install all dependencies
```bash
   pip install -r requirements.txt
```
**SQLite** - I used sqlite3 for the database. It is initialised with: 
```bash
   create_db.py
```
### Execution
Run the app.py: 
```bash
   python3 app.py
```

![UserManagement](https://user-images.githubusercontent.com/62619786/170845284-88b5e22a-8421-4c35-b6d9-1fefb14940e0.gif)

## Software Testing
Four type of tests have been implemented in this app [here](https://github.com/zeineblabbane/Software-Testing-Devops-Pipeline/tree/main/tests):
- Unit Testing: ``` tests/unit-tests  ```
- Integration Testing: ``` tests/integration-tests  ```
- E2E Testing: ``` tests/e2e-tests  ```
- UAT: ``` tests/uat-tests  ```

> You can run the tests manually or view the status of the tests in the pipeline.

## DevOps Pipeline
I built a CI/Cd pipeline using GitHub Actions, Docker and Amazon ECS.
### The overall Pipeline Schema:
![deployment](https://user-images.githubusercontent.com/62619786/172401913-75a87148-d33c-4574-bfbf-08e95767e301.PNG)

### Job 1: Test
Run Unit and Integration tests
### Job 2: Build
Build the Docker image and push it to [Docker Hub](https://hub.docker.com/repository/docker/zeineblabbane/user-management)
### Job 3: Deploy
Deploy the image to ECS with a service of 3 tasks definition.

> If the EC2 instance is still running, you can access the website [here](http://13.37.245.33:5000/)

![deployment_page](https://user-images.githubusercontent.com/62619786/172401959-59ab23ba-3c61-446c-9b25-66a36fe1298d.PNG)
