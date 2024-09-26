# Troubleshooting Guide

This document provides solutions to common issues you may encounter while using the Automated Resume Tailoring Tool.

## Table of Contents

1. [File & Directory Issues](#file--directory-issues)
2. [Environment & API Issues](#environment--api-issues)
3. [LaTeX Compilation Issues](#latex-compilation-issues)
4. [General Debugging Tips](#general-debugging-tips)

## File & Directory Issues

### **Issue**: "FileNotFoundError: No such file or directory"

**Cause**: This error typically occurs if the input files (`main.tex` or job description `.rtf`) are not in the correct location.

**Solution**:

- Ensure that the **base resume (`main.tex`)** is located at `OUTPUT_PATH`.
- Make sure that the **job description file** is stored at the path:

```

<OUTPUT_PATH>/<company>/<position>.rtf

```

- Double-check that the folder and file names match exactly (case-sensitive).

### **Issue**: "Missing Job Description"

**Cause**: The job description file for the specified position is not found or cannot be read.

**Solution**:

- Confirm that the `.rtf` file exists and is not corrupted.
- Ensure the file is saved in RTF format, not another format like `.txt` or `.docx`.
- Verify the file path and ensure that it matches the command-line input for `company` and `position`.

---

## Environment & API Issues

### **Issue**: "Invalid API Key" or "Authentication Error"

**Cause**: The OpenAI API key provided in the `.env` file is incorrect or missing.

**Solution**:

- Double-check the `OPENAI_API_KEY` value in your `.env` file.
- Make sure there are no extra spaces or line breaks around the key.
- If you suspect your key has been compromised or invalidated, generate a new key from the [OpenAI Dashboard](https://platform.openai.com/).

### **Issue**: "Rate Limit Exceeded"

**Cause**: The API request rate exceeds the limit of your OpenAI account.

**Solution**:

- Monitor your OpenAI account's API usage to ensure you are not exceeding rate limits.
- Implement delays or retries between API calls if necessary to manage usage.

---

## LaTeX Compilation Issues

### **Issue**: "File `fullpage.sty` not found" or Missing Package Errors

**Cause**: Your LaTeX distribution is missing some required packages for compilation.

**Solution**:

- Use the package manager for your LaTeX distribution (e.g., `tlmgr` for TeX Live or MacTeX) to install missing packages:

```bash
sudo tlmgr install fullpage
```

- Consider installing a complete LaTeX distribution if you are consistently facing missing packages:
  ```bash
  brew install mactex
  ```

### **Issue**: "PDF Compilation Failed"

**Cause**: An error in your `.tex` file or a LaTeX processing issue.

**Solution**:

- Run `pdflatex` manually to get more details on the error:
  ```bash
  pdflatex /path/to/yourfile.tex
  ```
- Check for errors in the `.tex` file, such as missing `\begin{document}` or `\end{document}` tags, or incorrect LaTeX syntax.
- Ensure that the `.tex` file does not contain any unintended lines or symbols that may cause errors.

### **Issue**: "Output PDF Not Created"

**Cause**: LaTeX compilation finished, but the `.pdf` was not generated.

**Solution**:

- Check that the `output_directory` exists and is writeable.
- Ensure there are no permission issues in your output path.

---

## General Debugging Tips

1. **Check Console Output for Errors**  
   Pay attention to any error messages printed in the console when running the tool, as they often provide clues on what went wrong.

2. **Clean Up Auxiliary Files**  
   If compilation fails repeatedly, try deleting the `aux_files/` directory and any auxiliary files, then recompile:

   ```bash
   rm -rf /path/to/output/aux_files/
   ```

3. **Validate `.env` Variables**

   - Ensure all environment variables are set correctly in the `.env` file.
   - Confirm that `OUTPUT_PATH` is correct and accessible.

4. **Manual Testing**  
   If errors persist, try running parts of the code manually:
   - **Check RTF Content**: Open the `.rtf` file and confirm its content is correctly formatted.
   - **Compile LaTeX Separately**: Run `pdflatex` manually on the `.tex` file to isolate LaTeX issues.

---

If none of the solutions resolve your issue, please consider checking the documentation for the libraries used (e.g., `OpenAI`, `striprtf`, LaTeX distribution) or submit a new issue on the GitHub repository.
