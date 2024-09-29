# Automated Resume Tailoring Tool

A Python-based tool for customizing LaTeX resumes based on job descriptions using the OpenAI API. The tool reads an existing `.tex` resume template, modifies it according to a provided job description, and generates a tailored LaTeX file and compiled PDF resume.

## Table of Contents

- [Automated Resume Tailoring Tool](#automated-resume-tailoring-tool)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Prepare Input Files](#prepare-input-files)
    - [Run the Tool](#run-the-tool)
    - [Output](#output)
  - [File Structure](#file-structure)
  - [Configuration](#configuration)
  - [Contributing](#contributing)
  - [License](#license)

## Project Overview

The Automated Resume Tailoring Tool streamlines the process of tailoring your LaTeX-based resume for different job applications. By leveraging the OpenAI API, this tool takes a job description from a URL as input and generates a personalized `.tex` file and a compiled `.pdf`.

## Features

- **Resume Customization**: Automatically modify your LaTeX resume based on the job description for the specific role.
- **PDF Extraction**: Downloads the job description as a PDF and extracts the text content.
- **LaTeX Compilation**: Generates a tailored `.tex` file and compiles it into a PDF.
- **Organized File Structure**: Manages input and output files, including auxiliary LaTeX files, for clean and easy access.

## Prerequisites

- **Python 3.x**: Required for running the tool and its dependencies.
- **LaTeX Distribution**: `pdflatex` is used to compile the `.tex` file into a `.pdf`.
- **OpenAI API Key**: An API key is required to access OpenAI's API for tailoring the resume content.
- **Google Chrome**: Needed for Selenium to extract PDF from job description URLs.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/automated-resume-tailoring.git
   cd automated-resume-tailoring
   ```

2. **Install Dependencies**

   Use `pip` to install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the root of the project directory and add your configuration details:

   ```dotenv
   OPENAI_API_KEY=<Your OpenAI API Key>
   OUTPUT_PATH=<Path where input/output files are stored>
   SYSTEM_ROLE=<System role for OpenAI API>
   ```

   Example:

   ```dotenv
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   OUTPUT_PATH=/Users/yourusername/Documents/resume-output
   SYSTEM_ROLE=Assistant for resume tailoring
   ```

## Usage

### Prepare Input Files

1. **Base Resume (`main.tex`)**:
   Place your LaTeX resume file in the directory specified by `OUTPUT_PATH`.

### Run the Tool

You can run the tool from either the project root or the `src/` directory:

- **From Project Root**:

  ```bash
  python -m src <company_name> <job_url>
  ```

  Example:

  ```bash
  python -m src Google "https://www.google.com/careers/job123"
  ```

- **From `src/` Directory**:

  ```bash
  cd src
  python main.py <company_name> <job_url>
  ```

  Example:

  ```bash
  python main.py Google "https://www.google.com/careers/job123"
  ```

### Output

- **Tailored LaTeX File**: `<OUTPUT_PATH>/<Date>/<CompanyName>/<PositionTitle>.tex`
- **Compiled PDF**: `<OUTPUT_PATH>/<Date>/<CompanyName>/<PositionTitle>.pdf`
- **Auxiliary LaTeX Files**: Moved to an `aux_files/` directory within each company's folder.

## File Structure

```
project_root/
├── .env
├── LICENSE.md
├── README.md
├── requirements.txt
├── docs/
│   ├── getting_started.md
│   ├── user_guide.md
│   ├── troubleshooting.md
│   ├── config.md
│   └── api_reference.md
├── src/
│   ├── __main__.py
│   ├── main.py
│   ├── resume_parser.py
│   ├── api_handler.py
│   ├── latex_compiler.py
│   └── utils.py
└── tests/                    # Unit tests (optional but recommended)
```

## Configuration

Make sure to set up your `.env` file correctly:

- **`OPENAI_API_KEY`**: Your OpenAI API key for accessing the API.
- **`OUTPUT_PATH`**: Directory path for input (LaTeX and job description files) and output (tailored `.tex` and `.pdf`).
- **`SYSTEM_ROLE`**: The context or role for the OpenAI assistant when tailoring the resume.

For more details on setting up and configuring the tool, refer to the [Getting Started](docs/getting_started.md) and [Config](docs/config.md) documents.

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and open pull requests.

1. **Fork the Repository**
2. **Create a Branch** (`git checkout -b feature/YourFeature`)
3. **Commit Changes** (`git commit -m 'Add Your Feature'`)
4. **Push to Branch** (`git push origin feature/YourFeature`)
5. **Open a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](docs/LICENSE.md) file for details.
