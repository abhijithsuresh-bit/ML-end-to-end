### Boston House Pricing Prediction

### Software and Tools Requirements

1. Github Account
2. HerokuAccount
3. VSCodeIDE

Create a new environment

'''
conda create -p end_ml python==3.10
'''

To activate the environment

'''
conda activate ./end_ml
'''

Install all the required Packages

'''
pip install -r requirements.txt
'''

We are deploying the web-app in heroku so that we need to create a 
'''
Procfile
'''
Procfile simply means when this web-app load what commands need to run 1st

Here the commands are related to gunicorn
gunicorn is the purest python https server for wsgi application it allows we to run python application concurrently by running multiple processes