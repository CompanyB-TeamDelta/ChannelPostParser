# helper script, that checks how many posts were retrieved at the moment.
# (in case of local posts storage)
import os
import json


def read_json_files_in_folder(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory.")
        return

    # Get a list of all files in the directory
    file_list = os.listdir(folder_path)

    # Filter JSON files
    json_files = [file for file in file_list if file.endswith(".json")]

    # Read content from each JSON file
    retrieved_posts = 0
    step = 0
    for json_file in json_files:
        step += 1
        print(f"In progress. step={step}")
        file_path = os.path.join(folder_path, json_file)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                retrieved_posts += len(data["posts"])
            except json.JSONDecodeError as e:
                print(f"Error reading {json_file}: {e}")
    print(f"Number of retrieved posts={retrieved_posts}")


if __name__ == "__main__":
    folder_path = "tmp/retrieved_data/"
    read_json_files_in_folder(folder_path)
