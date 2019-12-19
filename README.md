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

### Access

## TODO

### Django Apps TODO

- [ ] create django app for each sports
  - [ ] soccer
  - [ ] hockey
  - [ ] basketball
- [ ] create a django app for user
  - [ ] keeps track of login
  - [ ] " " " register
  - [ ] " " " sports they follow
  - [ ] can "bookmark" players they
  - [ ] provide route for them to look at statistics
- [ ] create django app for statistics
  - [ ] maybe could use Basyean Networks

### FrontEnd TODO

- [ ] for frontend of `/:sport/` create a map which hilights the city/state of each team
  - [ ] maybe do a league for soccer
- [ ] create endpoints for leagues `/:sport/:league`
- [ ] create endpoints for players `/player/:player_id (or slug)`
- [ ] on the homepage of the root app do the following:
  - [ ] highlight any upcoming matches (in the coming week)
  - [ ] highlight any ongoing matches
  - [ ] highlight all the sports offered
  - [ ] maybe look into news api to highlight news on sports

### Models TODO

- [ ] create a relational system for soccer
- [ ] create a generic one for player (may will make a players app)
- [ ] create a relational system for hocker
- [ ] create a relational system for basketball
- [ ] make admin/superusers

### Testing TODO

- [ ] learn about how to write tests for django

### Deploying TODO

- [ ] learn to deploy to heroku
  - [ ] check out the \$7/month hosting plan
- [ ] look at aws s3 hosting platform for static file (i.e. js/css files)
- [ ] look into getting google adsense
- [ ] look into getting domain name

### Misc TODO

- [ ] check out `https://www.sportmonks.com/` api (for free version its 180 calls per hour)
