### install virtual environment
virtualenv myenv


### activate virtual enironment
source ./myenv/Scripts/activate


### Deactivate the virtual environment 
deactivate

cd ERP_project/


----run server---
python manage.py runserver


### install all dependencies from requirements.txt 
pip install -r requirements.txt 

### save all dependencies in requirements.txt 
pip freeze > requirements.txt

## django version##
python -m django --version




echo "# school_managment" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/debajyoti1998/school_managment.git
git push -u origin main


git remote add origin https://github.com/debajyoti1998/school_managment.git
git branch -M main
git push -u origin main

----GIT UPDATE-------
git add .

git commit -m "..........."

git push -u origin main