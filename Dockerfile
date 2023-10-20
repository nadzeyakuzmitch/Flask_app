# Use a stable version of Python.
FROM python:3.8-slim-buster

# Set environment variables related to the QR code
ENV QR_CODE_IMAGE_DIRECTORY='static'
ENV QR_CODE_DEFAULT_URL='https://flask.palletsprojects.com/en/3.0.x/'
ENV QR_CODE_DEFAULT_FILE_NAME='default.png'

# Update the system packages and create a new user 'myuser'
RUN apt-get update && \
    apt-get -y install sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    adduser --disabled-password --gecos '' myuser

# Set the working directory
WORKDIR /home/myuser

# Copy the application files into the container
COPY . .

# Change the ownership of the files to 'myuser'
RUN chown -R myuser:myuser /home/myuser

# Switch to the non-root user
USER myuser

# Install the Python dependencies
RUN pip install -r requirements.txt

# Set the command to run your Flask application
ENTRYPOINT ["python", "app.py"]
