# algorithms

Algorithms for Fun and Profit

## Testing

To run unit tests a local python virtual environment should be configured. So, first create the virtual environment with the venv module and install the dependencies:

```
(from project home)
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

To run the unit tests:

```
export PYTHONPATH=$PWD/src
pytest -x -v src/test
```
