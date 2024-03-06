"""
Description: A program that reads through transaction records and reports the results.
Author: ACE Faculty
Edited by: Jasleen kaur
Date: 05-03-2024
Usage: This program will read transaction data from a .csv file, summarize and 
report the results.
"""
import csv
import os
from sqlite3 import Row
 
valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
valid_record = True
error_message = ''

os.system('cls' if os.name == 'nt' else 'clear')

try:
     with open('bank_data.csv', 'r') as csv_file:
         reader = csv.reader(csv_file)

        # Reset valid record and error message for each iteration
except FileNotFoundError as file_error:
     print(f"ERROR: {file_error} - The input file could not be located.")
     
except Exception as error:
    print(f"ERROR: {error} - An unexpected error occurred during program execution.")
    valid_record = True
    error_message = ''

 # Extract the customer ID from the first column
    customer_id = float(Row[0])


# code before data validation modifi
for row in reader:
        
        # Extract the transaction type from the second column
     ### VALIDATION 1 ###
    if row[1] not in valid_transaction_types:
         valid_record = False
         error_message += f"Invalid transaction type for Customer {row[0]}: {row[1]}. "
    

        # Extract the transaction amount from the third column
         
        ### VALIDATION 2 ###
try:       
    transaction_amount = float(row[2])
except ValueError:
     valid_record = False
     error_message += "Non-numeric transaction amount."

if valid_record:
            # Initialize the customer's account balance if it doesn't already exist
            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}

            # Update the customer's account balance based on the transaction type
            elif valid_transaction_types == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            elif valid_transaction_types == 'withdrawal':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
        
            # Record  transactions in the customer's transaction history
            customer_data[customer_id]['transactions'].append((transaction_amount, valid_transaction_types)) 
else:
        # Collect invalid records
        invalid_record_tuple = (row, error_message)
        rejected_records.append(invalid_record_tuple)
 
print("PiXELL River Transaction Report\n===============================\n")
# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"\nCustomer {customer_id} has a balance of {balance}.")
    # Print the transaction history for the customer
    print("Transaction History:")
    for transaction in data['transactions']:
        amount, type = transaction
        print(f"\t{type.capitalize()}: {amount}")

print(f"\nAVERAGE TRANSACTION AMOUNT: {(total_transaction_amount / transaction_counter)}")

print("\nREJECTED RECORDS\n================")
for record in rejected_records:
    print("REJECTED:", record)
