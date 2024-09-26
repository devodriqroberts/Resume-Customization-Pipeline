# Configuration Guide

This document provides details on how to configure the Automated Resume Tailoring Tool by setting up environment variables and managing file paths.

## Environment Variables

The tool relies on several environment variables to function properly. These should be set in a `.env` file located in the root directory of the project.

### **`.env` File Setup**

Create a `.env` file in your project directory:

```bash
touch .env
```

Add the following variables to the `.env` file:

```dotenv
OPENAI_API_KEY=<Your OpenAI API Key>
OUTPUT_PATH=<Path where input/output files are stored>
SYSTEM_ROLE=<System role for OpenAI API interactions>
```

### Variable Descriptions

- **`OPENAI_API_KEY`**:  
  Your API key for accessing the OpenAI API. This is required for making API calls to tailor your resume.

  - You can find or create your API key on the [OpenAI Dashboard](https://platform.openai.com/account/api-keys).
  - Example:
    ```dotenv
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

- **`OUTPUT_PATH`**:  
  The directory path where all input and output files (such as LaTeX resumes, job descriptions, and compiled PDFs) are stored.

  - This should be an absolute path (e.g., `/Users/yourusername/Documents/resume-output`).
  - Example:
    ```dotenv
    OUTPUT_PATH=/Users/yourusername/Documents/resume-output
    ```

- **`SYSTEM_ROLE`**:  
  The role or context provided to OpenAI during API interactions, used to tailor the resume content appropriately.
  - This can be a brief description of the role you want the OpenAI model to play when customizing your resume (e.g., "Assistant for resume tailoring").
  - Example:
    ```dotenv
    SYSTEM_ROLE=Assistant for resume tailoring
    ```

## Managing File Paths

The tool assumes a specific structure for your resume and job description files, all contained within the path specified by `OUTPUT_PATH`.

### Directory Structure

```
<OUTPUT_PATH>/
├── main.tex                      # Your base LaTeX resume
├── CompanyName/
│   ├── PositionTitle.rtf         # Job description for a specific position
│   └── PositionTitle.tex         # Generated tailored LaTeX file
│   └── PositionTitle.pdf         # Compiled tailored PDF resume
│   └── aux_files/                # Folder for auxiliary LaTeX files (generated during compilation)
```

### File Descriptions

- **`main.tex`**:  
  This is your base LaTeX resume file located directly in `OUTPUT_PATH`. The tool uses this file as a template to create tailored versions for specific job applications.

  - Place your `main.tex` file in the root of `OUTPUT_PATH`.

- **`<CompanyName>/<PositionTitle>.rtf`**:  
  Each job description should be saved as an `.rtf` file within a folder named after the company. The `.rtf` filename should match the job position.

  - For example, if you are applying for a Software Engineer position at Google, the file path should be:
    ```
    <OUTPUT_PATH>/Google/SoftwareEngineer.rtf
    ```

- **Output Files (`.tex` and `.pdf`)**:  
  After running the tool, the tailored resume and compiled PDF will be saved in the corresponding company folder.
  - **Tailored LaTeX File**: `<CompanyName>/<PositionTitle>.tex`
  - **Compiled PDF**: `<CompanyName>/<PositionTitle>.pdf`

## Auxiliary File Handling

During LaTeX compilation, several auxiliary files (e.g., `.aux`, `.log`, `.out`) are created. To keep the directory organized, the tool automatically moves these files into an `aux_files` subfolder within each company directory.

Example:

```
<OUTPUT_PATH>/Google/aux_files/
```

## Additional Configuration Notes

- **Environment Variable Changes**:  
  If you change any environment variables, make sure to reload them in your terminal or restart your Python script for changes to take effect.

- **File Path Issues**:  
  Ensure that the paths specified in your `.env` file and job description file structure are correct and accessible.

- **API Key Security**:  
  Keep your `OPENAI_API_KEY` secure and do not share it publicly. If you suspect your key is compromised, regenerate it from the OpenAI Dashboard.

By following these configurations, your environment will be correctly set up for the tool to function effectively.
