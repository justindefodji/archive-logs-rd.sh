
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run archive_logs.py when the container launches
ENTRYPOINT ["python", "archive_logs.py"]

# Example CMD arguments. These can be overridden by passing arguments via command line
CMD ["--archive", "/archive", "--days-old", "7"]
