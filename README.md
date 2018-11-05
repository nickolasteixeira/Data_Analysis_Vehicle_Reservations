# Turo Growth Challenge

Here at Turo we pride ourselves on being data-driven marketers. 
We study our customer data to understand their behaviors and determine the best ways to fuel growth

[Link to presentation](https://docs.google.com/presentation/d/1t9SDMGRa9Db1IY94bqjaCoiaMy6daHZz6xYriuldk2c/edit?usp=sharing) on Testing a new acquisition channel.


### Given two data sets (vehicles.csv and reservations.csv) find:
1. Which factors seem to be most important in driving total number of reservations for our vehicles

### General Hypothesis:
From a practical standpoint, it's my assumption that the price of a vehicles will be the most important factor driving the total number of reservations for a vehicle, followed by the number of images, and year of car. I believe that people want to get as much value as possible, while paying the least amount of money.

Let's analyse the datasets and come up with our own conclusion.  

### To run analysis, run docker container

### Requirements
1. [Install Docker](https://docs.docker.com/install/)


2. In your terminal in the directory for this repository, run:
`docker-compose up`
- This will output something like this in your terminal:
tarting datascience-notebook-container ... done
Attaching to datascience-notebook-container
```
datascience-notebook-container | /usr/local/bin/start-notebook.sh: ignoring /usr/local/bin/start-notebook.d/*
datascience-notebook-container |
datascience-notebook-container | Container must be run with group root to update passwd file
datascience-notebook-container | Executing the command: jupyter notebook
datascience-notebook-container | [W 00:26:28.432 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
datascience-notebook-container | [I 00:26:28.472 NotebookApp] JupyterLab beta preview extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
datascience-notebook-container | [I 00:26:28.472 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
datascience-notebook-container | [I 00:26:28.481 NotebookApp] Serving notebooks from local directory: /home/jovyan
datascience-notebook-container | [I 00:26:28.482 NotebookApp] 0 active kernels
datascience-notebook-container | [I 00:26:28.482 NotebookApp] The Jupyter Notebook is running at:
datascience-notebook-container | [I 00:26:28.482 NotebookApp] http://[all ip addresses on your system]:8888/?token=dfdfa78ab2a339dd88e4210eaf32050def83f66107b6d8d9
datascience-notebook-container | [I 00:26:28.483 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
datascience-notebook-container | [C 00:26:28.488 NotebookApp]
datascience-notebook-container |
datascience-notebook-container |     Copy/paste this URL into your browser when you connect for the first time,
datascience-notebook-container |     to login with a token:
datascience-notebook-container |         http://localhost:8888/?token=dfdfa78ab2a339dd88e4210eaf32050def83f66107b6d8d9
```

3. Look for the `localhost:8888` with a token value proceeding it
- Click on the link

4. Your `localhost:8888` should display a Jupyter notebook
- Click on the `Turo_analysis.ipynb` file

5. Read the Turo Analysis File
