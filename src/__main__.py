from src.main import main
import os
import argparse

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compile a LaTeX file and move auxiliary files.")
    parser.add_argument('company', type=str, help='Name of the company')
    parser.add_argument('position', type=str, help='Name of the position')

    # Parse the arguments
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.company, args.position)