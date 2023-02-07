FROM python:3.10.2

# Set the working directory in the container to /home/app
WORKDIR /home/app

# Copy the contents of the local directory Microservice1 to the container's /home/app directory
COPY modified_Microservice1.py .

# Install the dependencies from the requirements.txt file
RUN pip install Flask requests

# Expose port 5000 to the host
EXPOSE 5000


# Set the environment variable FLASK_APP to the name of your Flask application file
ENV FLASK_APP=modified_Microservice1.py

# Run the command "flask run" when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]