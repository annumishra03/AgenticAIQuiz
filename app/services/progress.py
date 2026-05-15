# Used to save data into JSON file
import json


# File path where progress data is stored
FILE_NAME = "data/progress.json"


# Function to save student feedback
def save_progress(feedback):

    try:
        # Open existing progress file
        with open(FILE_NAME, "+a") as f:

            # Load old data
            data = json.load(f)

    except:
        # If file doesn't exist,
        # start with empty list
        data = []

    # Add new feedback into list
    data.append(feedback)

    # Save updated data back into file
    with open(FILE_NAME, "+w") as f:

        json.dump(data, f, indent=4)

    print("Progress saved successfully")