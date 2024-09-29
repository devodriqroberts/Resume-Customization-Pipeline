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

# Install Chrome for selenium
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

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
