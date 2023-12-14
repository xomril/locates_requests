
# README for Locates Distribution Script

## Overview
This script is designed to process client requests for locates and distribute them based on available approved locates. The distribution is done proportionally based on the total requests for each symbol and the approved locates for that symbol.

## Key Functions
1. **request_locates**: This function simulates an API call to retrieve the approved locates for different symbols. The function returns a dictionary of symbols with their corresponding number of approved locates.

2. **distribute_locates**: This function takes two arguments, `client_requests` and `approved_locates`. It first calculates the total requested locates for each symbol and then distributes the approved locates to clients proportionally.

3. **main**: This is the main function of the script. It reads client requests from a CSV file (`locates_requests.csv`), aggregates these requests, calls `request_locates` to get approved locates, and then calls `distribute_locates` to distribute these locates. Finally, it writes the distribution results to another CSV file (`locates_distribution.csv`).

## Usage
1. Prepare a CSV file named `locates_requests.csv` with the following columns: `client_name`, `symbol`, and `number_of_locates_requested`.

2. Run the script. The script will read the input file, process the requests, and generate an output file named `locates_distribution.csv`.

3. The output file will contain columns: `client_name`, `symbol`, and `number_of_locates_approved`.

## Requirements
- Python 3
- CSV module (standard library)

## Notes
- This script is a prototype. The `request_locates` function currently returns a hardcoded dictionary and should be replaced with an actual API call.
- The distribution algorithm rounds down the allocated locates to the nearest hundred.
- Ensure that the input CSV file is formatted correctly to avoid errors.

## Example
**Input (locates_requests.csv):**
```
client_name,symbol,number_of_locates_requested
Client A,ABC,150
Client B,QQQ,50
```

**Output (locates_distribution.csv):**
```
client_name,symbol,number_of_locates_approved
Client A,ABC,150
Client B,QQQ,50
```
