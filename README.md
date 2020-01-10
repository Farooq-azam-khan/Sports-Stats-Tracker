# Sports Stats Tracker

## Setup

### Setup after cloning

1. install python (preferably version 3.8), and pipenv by typring `pip install pipenv`
2. `git clone [link]`
3. install pipenv: `pip install pipenv`
4. `pipenv install`
   - make sure this is done in the Pipfile directory
5. open the virtualenv: `pipenv shell`
6. `git branch [your-branch-name]`
7. `git checkout [your-branch-name]`
8. when pushing: `git push origin [your-branch-name]`
   - you will get the option to set-upstream.
   - copy that code and you will not need to write origin

### more info

- `https://www.youtube.com/watch?v=zDYL22QNiWk`
- installing dev dependencies: `pipenv install pytest --dev`
- un-installing dependencies: `pipenv uninstall`
- remove pipenv file completely: `pipenv --rm`

### First Time Setup

1. get python version 3.5+
   - recommended 3.8
2. get pipenv: `pip install pipenv`
3. cd into project folder
4. use `pipenv install django` to install Django
   - it will create a `Pipfile` in your project directory
   - the `Pipfile` is a replacement for the `requirements.txt` file one would have with virtualenv
   - it will tell you where the .virtualenvs file was made
5. To activate this project's virutalenv, run `pipenv shell`
   - if you just want to run a command in the environment run `pipenv run`

- used a restapi for django: https://www.django-rest-framework.org/#installation

* use `heroku pg` to check database records
