# Script to check if safes in current.csv still have an allocation in safe_user_allocations_reworked.csv

import pandas as pd

# Load current potential airdrop farming safes.
current = pd.read_csv('current.csv', index_col=0)
# Load current allocations
allocations = pd.read_csv('../safe_user_allocations_reworked.csv', index_col=0)

# List to collect safes already removed.
already_removed = []
# List to collect safes in current.csv that still have an allocation
available = []

# Iterate through current and check if the safes still have an allocation.
current.reset_index()
for index, row in current.iterrows():
    if index in allocations.index:
        print(index)
        available.append(index)
    else:
        already_removed.append(index)

print('{}/{} already removed.'.format(len(already_removed), len(current)))
print('{}/{} still available. (printed out above)'.format(len(available), len(current)))