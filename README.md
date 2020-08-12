# [tsundoku](https://en.wikipedia.org/wiki/Tsundoku) (積ん読)

### Getting Started

Dependences:

* Python 3.6
* MySQL `docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=password -d mysql:8.0` (requires docker)

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