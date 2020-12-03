# python-web-api
## 1.Prepare
#### 1.1 install [pyenv](https://github.com/pyenv/pyenv)
#### 1.2 install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
#### 1.3 set local python version.(3.9.0)
```
pyenv install 3.9.0 # if not installed
cd $projectRootDir
pyenv local 3.9.0
```
#### 1.4 create a new environment and activate
```
pyenv virtualenv $name
pyenv activate $name
pyenv local $name #If eval "$(pyenv virtualenv-init -)" is configured in your shell, pyenv-virtualenv will automatically activate/deactivate virtualenvs on entering/leaving directories which contain a .python-version file that contains the name of a valid virtual environment 
```
#### 1.5 install dependencies
```
pip install -r requirements.txt
```
## 2. execute
```
cd $projectRootDir
python manage.py runserver  
```

 