from datetime import datetime

# Assuming you have two timestamps as strings
timestamp1_str = "2024-04-11"
timestamp2_str = "2024-04-12"

# Convert the strings to datetime objects
timestamp1 = datetime.strptime(timestamp1_str, "%Y-%m-%d")
timestamp2 = datetime.strptime(timestamp2_str, "%Y-%m-%d")

# Compare the timestamps
if timestamp1 < timestamp2:
    print("Timestamp 1 is earlier than Timestamp 2")
elif timestamp1 > timestamp2:
    print("Timestamp 1 is later than Timestamp 2")
else:
    print("Timestamp 1 and Timestamp 2 are equal")