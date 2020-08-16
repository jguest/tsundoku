# [tsundoku](https://en.wikipedia.org/wiki/Tsundoku) (積ん読)

### Getting Started

Dependences:

* Python 3.6
* MySQL

MySQL Mac Install:

```bash
brew install mysql
brew services start mysql
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY <YOUR_PASS>;
```

Virtual Environment:

```bash
cd tsundoku/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

PyCharm Setup:

* Open this project
* Setup 3.6, project-level interpreter
* Create run configuration
* Enjoy!