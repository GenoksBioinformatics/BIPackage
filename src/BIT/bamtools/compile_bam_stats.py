import os
import pandas as pd
import argparse

'''Script can compile detailed bam statistics produced by Megabolt'''

def parse_coverage_report(file_path):
    """Parse a .coverage.report file and return a dictionary of its contents."""
    data = {}
    
    sample_name = os.path.basename(file_path).split('.')[0]  # Extract sample name from filename
    data["Sample"] = sample_name
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines[2:]:  # Skip the first two lines
            parts = line.strip().split()  # Splitting based on whitespace
            if len(parts) >= 2:
                key = ' '.join(parts[:-1])  # Key is everything except the last element
                value = parts[-1]  # Value is the last element
                data[key] = str(value)  # Store values as strings to prevent conflicts
    
    return data

def find_coverage_report_files(root_dir):
    """Recursively find all .coverage.report files in a directory."""
    report_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".coverage.report"):
                report_files.append(os.path.join(root, file))
    return report_files

def compile_reports_to_csv(root_dir, output_csv):
    """Compile all .coverage.report files into a single CSV."""
    report_files = find_coverage_report_files(root_dir)
    data_list = [parse_coverage_report(file) for file in report_files]
    df = pd.DataFrame(data_list)
    df.to_csv(output_csv, index=False)
    print(f"Compiled {len(report_files)} files into {output_csv}")

def main():
    parser = argparse.ArgumentParser(description="Compile coverage report files into a CSV.")
    parser.add_argument("root_directory", type=str, help="Root directory to scan for .coverage.report files")
    parser.add_argument("output_csv", type=str, help="Path to output CSV file")
    args = parser.parse_args()
    compile_reports_to_csv(args.root_directory, args.output_csv)

if __name__ == "__main__":
    main()