# Getting Started

This guide will help you set up and run the Automated Resume Tailoring Tool. The tool customizes LaTeX resumes based on job descriptions and generates a tailored `.tex` file and PDF.

## Prerequisites

### 1. Install Python and LaTeX Distribution

- **Python 3.x**: Make sure Python is installed on your machine.

  - Check your Python version:
    ```bash
    python --version
    ```
  - [Download Python](https://www.python.org/downloads/) if not installed.

- **LaTeX Distribution**: You need `pdflatex` for compiling `.tex` files into PDFs.
  - On macOS, you can install `basictex` using Homebrew:
    ```bash
    brew install basictex
    ```
  - Alternatively, download and install [MacTeX](https://www.tug.org/mactex/).

### 2. Install Git (Optional)

If you plan to clone the repository, install Git:

```bash
brew install git
```

## Project Structure

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
│   ├── pdf_generator.py
│   ├── api_handler.py
│   ├── latex_compiler.py
│   └── utils.py
└── tests/                    # Unit tests (optional but recommended)
```

## Installation

### 1. Clone the Repository

Clone the GitHub repository to your local machine:

```bash
git clone https://github.com/devodriqroberts/Resume-Customization-Pipeline.git
cd automated-resume-tailoring
```

### 2. Install Python Dependencies

Make sure you have `pip` installed, then install all required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory to store your environment variables.

```bash
touch .env
```

Add the following variables to your `.env` file:

```dotenv
OPENAI_API_KEY=<Your OpenAI API Key>
SYSTEM_ROLE_POSITION=<Role for extracting position>
SYSTEM_ROLE_<SECTION>=<Role for tailoring each resume section>
SYSTEM_LATEX_DOC_STRUCTURE=<Role for LaTeX structure>
```

- **`OPENAI_API_KEY`**: Your API key from OpenAI.
- **`OUTPUT_PATH`**: The absolute path to the directory where input and output files are stored.
- **`SYSTEM_ROLE`**: The role/context provided to the OpenAI model during API interactions.

**Example**:

```dotenv
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OUTPUT_PATH=/Users/yourusername/Documents/resume-output
SYSTEM_ROLE=Assistant for resume tailoring
```

## Preparing Input Files

1. **`main.tex`**: Place your base LaTeX resume at `<OUTPUT_PATH>/main.tex`.
2. **Job Descriptions**:
   Store .pdf job descriptions in folders as:
   ```
   <OUTPUT_PATH>/<date>/<company>/<position>/job_description.pdf
   ```

**Example Directory Structure**:

```
<OUTPUT_PATH>/
├── latex-resume/
│   └── main.tex
├── <date>/
│   └── Google/
│       └── software_engineer/
│           └── job_description.pdf
```

## Running the Tool

You can run the tool either from the project root using the `src` module or directly from `src/main.py`.

### Option 1: Running from Project Root

Run the following command from the project root:

```bash
python -m src <company_name> <job_url>
```

- Replace `<company_name>` with the company you're applying to.

**Example**:

```bash
python -m src Google "https://jobs.google.com/12345"
```

### Option 2: Running from `src` Directory

Alternatively, navigate to the `src` directory and run:

```bash
cd src
python main.py <company_name> <job_url>
```

**Example**:

```bash
python main.py Google "https://jobs.google.com/12345"
```

## Output

- **Tailored LaTeX File**: ` <OUTPUT_PATH>/<date>/<company>/<position>/<position>.tex`
- **Compiled PDF**: `<OUTPUT_PATH>/<date>/<company>/<position>/<position>.pdf`
- **Auxiliary LaTeX Files**: Moved to an `aux_files/` directory inside `<OUTPUT_PATH>/<date>/<company>/<position>`.

## Troubleshooting

- If LaTeX compilation fails, ensure all necessary LaTeX packages are installed.
- Verify that the `.env` file is correctly set with all required variables.
- Check the correct paths for input files (main.tex, job description PDFs).
