FROM python:3.8-slim-buster

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
