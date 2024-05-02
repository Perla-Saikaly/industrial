# Use the official Python 3.11.8 image as the base image
FROM python:3.11.8


# Optionally, set the working directory
WORKDIR /app
 
# Copy your Python application code into the container
COPY . /app



# Install any dependencies using pip
RUN pip install -r requirements.txt

EXPOSE 8002
 
# Set the entry point or command to run when the container starts
CMD ["python", "/app/handwritten.py"]
