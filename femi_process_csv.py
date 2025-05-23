"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
Process a CSV file on 2020 Happiness ratings by country to analyze the `Healthy life expectancy` and `Logged GDP per capita` 
columns and save statistics.
This script reads a CSV file, calculates the minimum, maximum, mean, and standard deviation of the `Healthy life expectancy` 
and `Logged GDP per capita` columns,

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "femi_data"
PROCESSED_DIR: str = "femi_processed_data"

#####################################
# Define Functions
#####################################


def analyze_columns(file_path: pathlib.Path, columns: list) -> dict:
    """Analyze specified columns to calculate min, max, mean, and stdev."""
    try:
        results = {col: [] for col in columns}
        
        with file_path.open('r') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                for col in columns:
                    try:
                        value = float(row[col])
                        results[col].append(value)
                    except (ValueError, KeyError) as e:
                        logger.warning(f"Skipping invalid {col} in row: {row} ({e})")
        
        stats = {}
        for col in columns:
            if results[col]:
                stats[col] = {
                    "min": min(results[col]),
                    "max": max(results[col]),
                    "mean": statistics.mean(results[col]),
                    "stdev": statistics.stdev(results[col]) if len(results[col]) > 1 else 0,
                }
        return stats
    
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Process CSV file and save statistics for t`Healthy life expectancy` and `Logged GDP per capita` columns."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2020_happiness.csv")
    columns_to_analyze = ["Healthy life expectancy", "Logged GDP per capita"]
    
    # Get statistics
    stats = analyze_columns(input_file, columns_to_analyze)
    
    # Save results to separate files
    output_dir = pathlib.Path(PROCESSED_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for col in columns_to_analyze:
        if col in stats:
            output_file = output_dir / f"{col.lower().replace(' ', '_')}_stats.txt"
            # Open the output file in write mode and write the results
            with output_file.open('w') as f:
                f.write(f"{col} Statistics:\n")
                f.write(f"Minimum: {stats[col]['min']:.2f}\n")
                f.write(f"Maximum: {stats[col]['max']:.2f}\n")
                f.write(f"Mean: {stats[col]['mean']:.2f}\n")
                f.write(f"Standard Deviation: {stats[col]['stdev']:.2f}\n")
            # Log the processing of the CSV file
            logger.info(f"Processed {col} statistics saved to: {output_file}")
            # logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")