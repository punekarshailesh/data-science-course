import json

# Function to convert txt file with key=value pairs into a JSON object
def convert_txt_to_json(file_path):
    data = {}

    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)  # Split by the first '=' found
            data[key] = value

    return data

# Path to your .txt file
file_path = 'q-multi-cursor-json.txt'

# Convert to JSON format
json_data = convert_txt_to_json(file_path)

# Print the JSON object
print(json.dumps(json_data, indent=4))  # Pretty print JSON

# Optional: Save to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
