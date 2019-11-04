FROM python:3

RUN git clone https://github.com/JJHernandez99/sudoku

WORKDIR /sudoku

RUN pip freeze > requirements.txt

RUN pip install parametrized

RUN pip install requests

RUN pip install -r requirements.txt

CMD ["python", "./Interfaz.py"]