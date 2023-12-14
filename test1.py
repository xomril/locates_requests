import csv

def request_locates():
    # This function should be replaced with the actual API call.
    approved_locates = {' ABC': 300, ' QQQ': 100, ' TTT': 100}
    return approved_locates

def distribute_locates(client_requests, approved_locates):
    # Calculate total requested locates for each symbol
    total_requested = {symbol: 0 for symbol in approved_locates}
    for request in client_requests:
        total_requested[request['symbol']] += request['number_of_locates_requested']

    # Distribute locates to clients
    distributed_locates = []
    for request in client_requests:
        symbol = request['symbol']
        if symbol in approved_locates and total_requested[symbol] > 0:
            proportion = request['number_of_locates_requested'] / total_requested[symbol] 
            allocated = int((approved_locates[symbol] * proportion) // 100 * 100)
            distributed_locates.append({
                'client_name': request['client_name'],
                'symbol': symbol,
                'number_of_locates_approved': min(allocated, request['number_of_locates_requested'])
            })

    return distributed_locates

def main():
    client_requests = []
    with open('locates_requests.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            client_requests.append({
                'client_name': row['client_name'],
                'symbol': row['symbol'],
                'number_of_locates_requested': int(row['number_of_locates_requested'])
            })
    # Aggregate requests
    aggregated_requests = {}
    for request in client_requests:
        symbol = request['symbol']
        aggregated_requests[symbol] = aggregated_requests.get(symbol, 0) + request['number_of_locates_requested']

    # Call request_locates function
    approved_locates = request_locates()

    # Distribute locates
    distributed_locates = distribute_locates(client_requests, approved_locates)

    # Output results
    with open('locates_distribution.csv', mode='w', newline='') as file:
        fieldnames = ['client_name', 'symbol', 'number_of_locates_approved']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for locates in distributed_locates:
            writer.writerow(locates)

    print("Locates distribution completed. Check locates_distribution.csv for details.")

if __name__ == "__main__":
    main()
