# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && rm /code/requirements.txt

# TODO: WIP here fix the path
COPY ./src /code/app

# run the starting point of the application
CMD ["python","/code/app/backend/main.py"]
