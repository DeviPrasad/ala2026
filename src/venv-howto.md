# Installation Instructions

These are the recommended version of the packages as on 10 June 2026.

- Python 3.12.x (less than 3.14).
- Numpy < 2, meaning Numpy 1.26.4
- Pytorch 2.2.2


```bash
python3.12 -m venv linalg
source linalg/bin/activate

pip install numpy==1.26.4

pip install torch==2.2.2
```

## Check the Dependencies and Version Information

```python
pip freeze > requirements.txt
```
