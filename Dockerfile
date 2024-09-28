# Use the full Python image for better support
FROM python:3.12

# Install necessary system packages for LaTeX installation
RUN apt-get update && apt-get install -y \
    wget \
    perl \
    tar \
    xz-utils \
    gnupg \
    ca-certificates \
    --no-install-recommends

# Install LaTeX (BasicTeX equivalent)
RUN apt-get update && apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to install Python dependencies
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . .

# Command to run your app (adjust arguments as needed)
ENTRYPOINT ["python", "-m", "src"]
