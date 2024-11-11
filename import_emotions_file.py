import re

def import_file(file_path):
    entries = []

    # Define the regex pattern
    pattern = r"Date:\s*(\d{2})/(\d{2})/(\d{4})\nEmotion:\s*(.*?)\nEntry:\s*(.*)"

    with open(file_path, 'r') as file:
        file_content = file.read()  # Read the entire content of the file

        # Perform the regex search on the entire content
        match = re.search(pattern, file_content)

        # If there's a match, extract the data
        if match:
            date_month = match.group(1)
            date_day = match.group(2)
            date_year = match.group(3)
            emotion = match.group(4)
            entry = match.group(5)
            date_str = f"{date_month}/{date_day}/{date_year}"
            
            # Append validated and processed entry
            entries.append({"Date": date_str, "Emotion": emotion, "Entry": entry})

    return entries

# Example usage
# result = import_file('path/to/your/input_file.txt')
# print(result)