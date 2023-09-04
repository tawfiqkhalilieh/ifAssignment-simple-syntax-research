import json
import matplotlib.pyplot as plt
import os
import json


# Define the base directory to start the search
base_directory = 'code/'  # Replace with the actual path

# Initialize an empty dictionary to store the results
results_dict = {}

# Function to process each directory
def process_directory(directory_path):
    # Check if "results.json" exists in the directory
    results_file = os.path.join(directory_path, "results.json")
    if os.path.exists(results_file):
        # Load the JSON data from "results.json"
        with open(results_file, "r") as file:
            data = json.load(file)
        # Store the data in the results_dict
        results_dict[directory_path.replace("code/", '')] = data.get("result", {})

# Walk through the directory tree and process each directory
for root, dirs, files in os.walk(base_directory):
    for directory in dirs:
        directory_path = os.path.join(root, directory)
        process_directory(directory_path)


# Count the occurrences of each value
data_counts = {}

print(results_dict)
for value in results_dict.values():
    if value in data_counts:
        data_counts[value] += 1
    else:
        data_counts[value] = 1

# Extract labels and counts for plotting
labels = list(data_counts.keys())
counts = list(data_counts.values())

# Create a bar chart
plt.bar(labels, counts)

# Add labels and title
# plt.xlabel('Values')
# plt.ylabel('Counts')
plt.title('Results')

# Save the plot as "results.png"
plt.savefig('results.png')

# # Show the plot (optional)
# plt.show()