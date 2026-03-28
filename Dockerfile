# Base image
FROM python:3.11-slim

# Install required libraries
RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

# Create working directory inside container
WORKDIR /app/pipeline/

# Copy all project scripts into the container
COPY . .

# Start an interactive bash shell when container runs
CMD ["bash"]