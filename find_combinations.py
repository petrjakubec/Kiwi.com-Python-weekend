#!/usr/bin/env python3

# Author: Petr Jakubec
# Date: 2016-09-15
# Project: Assignment to Kiwi Python weekend
# Find combinations in a database of flights with a given restrictions

import csv
from sys import stdin
from datetime import datetime
from datetime import timedelta

# Function to search for flights available from origin
def search_flights(source, arrival, flight_list, iteration):
    # Iterate through all flights
    for flight in all_flights:
        # Handling time restrictions - flights should be between 1 and 4 hours
        parse_time = datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')
        added_hour = parse_time + timedelta(hours = 1) # arrival + 1 hour
        added_four_hours = parse_time + timedelta(hours = 4) # arrival + 4 hours
        ftime = datetime.strptime(flight[2], '%Y-%m-%dT%H:%M:%S')

        # Check if we're in source destination and the times match
        if source == flight[0] and added_hour <= ftime and added_four_hours >= ftime:
            # Check if we've not come across invalid combination - A->B->A->B
            if {"source":flight[0],"destination":flight[1]} not in flight_list:
                # Add to the list of (source, destination) combinations
                flight_list.append({"source":flight[0],"destination":flight[1]})
                # Print the result on the output
                print("         ","   "*iteration,flight[0],"->",flight[1],"("+flight[4]+")")
                # Call the function recursively
                search_flights(flight[1], flight[3], flight_list,iteration+1)
                # Remove from the list of (source, destination) combinations once we're done with the branch
                flight_list.remove({"source":flight[0],"destination":flight[1]})

# Discard first line of the csv
stdin.readline()

# Read contents from STDIN
readCSV = csv.reader(stdin, delimiter=',')

# Variable that stores all information about flights
all_flights = []

# Load the all_flights variable with rows from STDIN
for row in readCSV:
    all_flights.append(row)

# Find all combinations of the flights and print wanted output
for current in all_flights:
    print("####################################################")
    print("Origin:",current[0],"->",current[1],"("+current[4]+")")
    # We're currently on the first level, let's search deeper
    search_flights(current[1], current[3], [{"source":current[0],"destination":current[1]}], 0)
    print()