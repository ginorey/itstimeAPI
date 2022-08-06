# choose python image
FROM python:3.9-slim-buster

# working directory
WORKDIR /itstimeapi

# install dependencies
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy directory 
COPY . .

# Run container on port 5000
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000