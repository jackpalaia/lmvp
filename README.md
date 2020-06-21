<!-- [![Build Status](https://travis-ci.org/abhinavtripathy/XAuth.svg?branch=master)](https://travis-ci.org/abhinavtripathy/XAuth) -->
[![License](https://img.shields.io/badge/License-BSD%203%20Clause-brightgreen.svg)](./LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/dsc-umass/lmvp.svg?color=red)
![GitHub stars](https://img.shields.io/github/stars/dsc-umass/lmvp.svg)

# LMVP

> Lightweight Model Versioning Platform

## About
An open source neural network versioning system designed to separate model management functions and computationally expensive training operations.

## Getting Started
[Docker Compose](https://docs.docker.com/compose/install/) is the recommended way to run the API server. After cloning or downloading the repository, run `docker-compose run web python3 manage.py migrate` to build the initial tables in thedatabase. Then run `docker-compose up` to start LMVP. From there, you can navigate to the server in a web browser to see the Django Rest Framework interface, or use another tool to make API requests.

## Features

- Fetch, update, and publish models from anywhere
- Track metrics
- Manage model history on the web
- Add team members, make contributions

### Example commands
```
>>> localModel = lmvp.download(modelName)
```
```
>>> lmvp.showHistory(project)
```
```
>>> lmvp.update(modelname, localModel)
```

## Task Groups
Commits addressing issues in a group may now be added to the corresponding branch. The *dev* branch may be used for generating test builds, which are available at the Docker repository `jbinvnt/lmvp:latest`. The *master* branch gets built at `jbinvnt/lmvp:stable` and should be used once features have been tested.

Issues for each group are available in the *Projects* tab.

| Group | Features |
| --- | --- |
| client | Utilities such as Python modules to allow team members to transfer models to/from the central server. |
| versioning | System for keeping track of how models and weights change over time. |
| webapp | The web administrator console. Built using Django, frontend framework TBD. |

## Comparison with other platforms
![Traditional Cloud Worlflow](/docs/images/TraditionalCloudWorkflow.PNG?raw=true)
![Local Training Workflow](/docs/images/LocalTrainingWorkflow.PNG?raw=true)
