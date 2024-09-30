FROM python:3.12

# Install necessary system packages
RUN apt-get update && apt-get install -y wget ca-certificates gnupg

# Install Playwright and browsers
RUN pip install playwright && playwright install && playwright install-deps 

# Install LaTeX (BasicTeX equivalent)
RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .
ENV DOCKER_USE=1

# Command to run your app (adjust arguments as needed)
ENTRYPOINT ["python", "-m", "src"]