# User Guide

This guide provides detailed instructions on how to use the Automated Resume Tailoring Tool to customize your LaTeX resume based on job descriptions. It covers setting up input files, running the tool, and handling outputs.

## Table of Contents

- [User Guide](#user-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Understanding the Workflow](#understanding-the-workflow)
  - [Setting Up the File Structure](#setting-up-the-file-structure)
  - [Running the Tool](#running-the-tool)
    - [Option 1: Run from Project Root](#option-1-run-from-project-root)
    - [Option 2: Run from `src/` Directory](#option-2-run-from-src-directory)
  - [Configuring the Environment](#configuring-the-environment)
    - [`.env` File Setup](#env-file-setup)
  - [Understanding the Output](#understanding-the-output)
    - [Example Directory Structure Post-Run](#example-directory-structure-post-run)
  - [Troubleshooting \& Tips](#troubleshooting--tips)
    - [Common Issues](#common-issues)
    - [Useful Tips](#useful-tips)

## Overview

The Automated Resume Tailoring Tool allows you to customize your LaTeX resume based on specific job descriptions. It uses OpenAI's API to generate tailored content and outputs a `.tex` file and a compiled PDF.

## Understanding the Workflow

1. **Base Resume Template**:  
   The tool uses a LaTeX `.tex` file (`main.tex`) as the starting point for generating tailored resumes.

2. **Job Description Input**:  
   The tool takes a job description file (`.rtf`) stored in a specific folder structure (`<OUTPUT_PATH>/<company>/<position>.rtf`).

3. **Customization Process**:  
   The tool interacts with the OpenAI API to modify the base resume according to the provided job description and then compiles the tailored `.tex` into a PDF.

## Setting Up the File Structure

Ensure your files are organized as follows:

```

<OUTPUT_PATH>/
├── main.tex # Base LaTeX resume
├── <CompanyName>/
│ ├── <PositionTitle>.rtf # Job description for a specific position
│ ├── <PositionTitle>.tex # Generated tailored LaTeX file
│ ├── <PositionTitle>.pdf # Compiled tailored PDF resume
│ └── aux_files/ # Folder for auxiliary LaTeX files (generated during compilation)

```

- **`main.tex`**: The base LaTeX resume file located directly in `OUTPUT_PATH`.
- **Job Descriptions**: Each job description is saved as an `.rtf` file within a folder named after the company, with the filename being the job position title.

**Example**:

```

/Users/yourusername/Documents/resume-output/
├── main.tex
├── Google/
│ ├── SoftwareEngineer.rtf
│ ├── SoftwareEngineer.tex
│ ├── SoftwareEngineer.pdf
│ └── aux_files/

```

## Running the Tool

The tool can be executed either from the project root using the `src` module or directly from `src/main.py`.

### Option 1: Run from Project Root

Navigate to the root directory of your project and run:

```bash
python -m src <company_name> <position_name>
```

- Replace `<company_name>` with the name of the company.
- Replace `<position_name>` with the job title.

**Example**:

```bash
python -m src Google SoftwareEngineer
```

### Option 2: Run from `src/` Directory

Alternatively, you can run the tool directly from the `src` directory:

```bash
cd src
python main.py <company_name> <position_name>
```

**Example**:

```bash
python main.py Google SoftwareEngineer
```

## Configuring the Environment

### `.env` File Setup

Ensure that the `.env` file is correctly configured with the necessary environment variables:

```dotenv
OPENAI_API_KEY=<Your OpenAI API Key>
OUTPUT_PATH=<Path to the directory where files are stored>
SYSTEM_ROLE=<Role for OpenAI API interactions>
```

- **`OPENAI_API_KEY`**: Your OpenAI API key for authentication.
- **`OUTPUT_PATH`**: The directory path where input and output files are stored.
- **`SYSTEM_ROLE`**: Describes the role/context for OpenAI when generating responses.

## Understanding the Output

After running the tool, you will find the following files generated in the `<OUTPUT_PATH>/<company_name>/` directory:

- **`<PositionTitle>.tex`**: The tailored LaTeX resume based on the provided job description.
- **`<PositionTitle>.pdf`**: The compiled PDF version of the tailored resume.
- **`aux_files/` Folder**: Contains auxiliary files generated during LaTeX compilation (e.g., `.aux`, `.log`).

### Example Directory Structure Post-Run

```
/Users/yourusername/Documents/resume-output/
├── main.tex
├── Google/
│   ├── SoftwareEngineer.rtf
│   ├── SoftwareEngineer.tex
│   ├── SoftwareEngineer.pdf
│   └── aux_files/
│       ├── SoftwareEngineer.aux
│       ├── SoftwareEngineer.log
│       └── ...
```

## Troubleshooting & Tips

### Common Issues

1. **LaTeX Compilation Errors**:

   - Ensure you have all the necessary LaTeX packages installed.
   - Check for syntax errors in the LaTeX file.

2. **Environment Variables Not Set**:

   - Make sure all environment variables are correctly set in your `.env` file.
   - Verify that `OUTPUT_PATH` is correct and accessible.

3. **Job Description Not Found**:

   - Check that the `.rtf` file is named and located correctly as `<company>/<position>.rtf`.

4. **OpenAI API Errors**:
   - Verify that your `OPENAI_API_KEY` is valid and has sufficient permissions.
   - Monitor your OpenAI account for API usage and rate limits.

### Useful Tips

- **Tailor Multiple Resumes**:  
  You can run the tool multiple times for different companies and positions. Just ensure each job description is correctly named and placed within its respective folder.

- **Clean Up Auxiliary Files**:  
  Auxiliary files are moved to an `aux_files/` folder automatically. If you encounter any issues, try deleting this folder and re-running the tool.

---

By following this guide, you can efficiently use the Automated Resume Tailoring Tool to create tailored resumes for various job applications. For more details or troubleshooting, refer to other documentation in the `docs/` directory.
