FROM python:3.9-slim-buster

# To Set the working directory in the container
WORKDIR /app

# To Copy the local code directory to the container
COPY . /app

# To Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# To Set the environment variable
ENV FLASK_APP=app.py

# To Expose port 5000 to allow communication to/from server
EXPOSE 5000

# To Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]