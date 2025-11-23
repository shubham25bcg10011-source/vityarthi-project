# vityarthi-project

# Lost & Found Management System

## Overview
This is a simple command-line application designed to help users report, track, and manage lost and found items. The system provides an efficient and organized way to handle both lost and found records, allowing users to add, search, update, and maintain items with ease.

## Features
- Report lost or found items with details like item name, location, contact, and notes
- View lists of all lost and found items
- Search for items by name or location
- Mark lost items as claimed and found items as returned
- Edit and delete existing item records
- Undo the last deletion action
- Save data persistently in a JSON file for consistency between sessions
- Interactive command-line menu system with clear prompts and validations

## Technologies & Tools Used
- Python 3
- Standard libraries: `json`, `os`, `datetime`
- JSON file handling for data persistence
- Command-line interface for user interaction

## Installation & Running the Project
1. Make sure Python 3 is installed on your system.
2. Save the provided Python script (`lost_found.py`) to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script with:


## Testing Instructions
- Use the interactive menu to test various functionalities:
- Add lost or found items and verify they appear in the respective lists.
- Search for items by partial or full keywords in item names or places.
- Mark items as claimed or returned and check status updates.
- Edit entries to correct or update information.
- Delete items and use the undo option to restore the last deletion.
- Invalid inputs will prompt error messages, ensuring robustness.
- Test saving and loading data by restarting the application and confirming persistence.

---

Feel free to customize or expand this README for your project's hosting or documentation needs.
