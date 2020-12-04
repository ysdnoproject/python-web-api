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
## 2. Test
#### 2.1 start server
```
cd $projectRootDir
uvicorn main:app --reload
```
#### 2.2 
visit 
[http://127.0.0.1:8000/threads]() to show all threads
#### 2.3
visit 
[http://127.0.0.1:8000/thread/create]() to create a new thread
#### 2.4
visit 
[http://127.0.0.1:8000/thread/$ident/delete]() to delete a thread
 