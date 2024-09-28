from src.main import main
import os
import argparse

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compile a LaTeX file and move auxiliary files.")
    parser.add_argument('company', type=str, help='Company name')
    parser.add_argument('job_url', type=str, help='URL of job description')

    # Parse the arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.company, args.job_url)