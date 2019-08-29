
1. Forgot to run `pipenv shell` to activate the virtualenv;
2. then install some Python packages;
3. Pipfile.lock has some problem;
4. Delete Pipfile and Pipfile.lock in the project folder, delete virtualenv folder;
5. Re-create virtualenv again.

```
(base) PS D:\lambdaschool> cd .\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes\
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> ls


    Directory: D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       2019-08-24  12:39 PM                datasets
d-----       2019-08-24  12:45 PM                notebooks
-a----       2019-08-23  11:45 PM           1100 LICENSE
-a----       2019-08-27  02:39 PM           1882 README.md


(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv install
Creating a virtualenv for this project�
Pipfile: D:\LambdaSchool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes\Pipfile
Using c:\users\*\anaconda3\python.exe (3.7.3) to create virtualenv�
[   =] Creating virtual environment...Already using interpreter c:\users\*\anaconda3\python.exe
Using base prefix 'c:\\users\\*\\anaconda3'
New python executable in C:\Users\*o\.virtualenvs\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes-WHMmWEFm\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\*\.virtualenvs\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes-WHMmWEFm
Creating a Pipfile for this project�
Pipfile.lock not found, creating�
Locking [dev-packages] dependencies�
Locking [packages] dependencies�
Updated Pipfile.lock (a65489)!
Installing dependencies from Pipfile.lock (a65489)�
  ================================ 0/0 - 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv install pandas numpy
Installing pandas�
Adding pandas to Pipfile's [packages]�
Installation Succeeded
Installing numpy�
Adding numpy to Pipfile's [packages]�
Installation Succeeded
Pipfile.lock (8a0daf) out of date, updating to (a65489)�
Locking [dev-packages] dependencies�
Locking [packages] dependencies�
Success!
Updated Pipfile.lock (8a0daf)!
Installing dependencies from Pipfile.lock (8a0daf)�
  ================================ 5/5 - 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv run pip freeze > requirements.txt
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv install flask
Installing flask�
[====]Adding Installing... flask to Pipfile's [packages]�
Installation Succeeded
Pipfile.lock (b443a2) out of date, updating to (8a0daf)�
Locking [dev-packages] dependencies�
Locking [packages] dependencies�
Success!
Updated Pipfile.lock (b443a2)!
Installing dependencies from Pipfile.lock (b443a2)�
  ================================ 11/11 - 00:00:04
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv install scikit-learn
Installing scikit-learn�
Adding scikit-learn to Pipfile's [packages]�
Installation Succeeded
Pipfile.lock (1f873c) out of date, updating to (b443a2)�
Locking [dev-packages] dependencies�
Locking [packages] dependencies�
Success!
Updated Pipfile.lock (1f873c)!
Installing dependencies from Pipfile.lock (1f873c)�
  ================================ 14/14 - 00:00:05
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes> pipenv run pip freeze > requirements.txt
(base) PS D:\lambdaschool\DS-Unit-3-Sprint-4-Build-Week-Safe-Routes>
```
