import os
import json
from datetime import datetime

class HistoryData:
    def __init__(self, file_name='history.json'):
        self.file_name = file_name
        self.data = self.load_data()

    def load_data(self):
        """Load historical data from file"""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        """Save the current data to file"""
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_entry(self, entry):
        """Add a new entry to the history"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data.append({"timestamp": timestamp, "entry": entry})
        self.save_data()

    def get_history(self):
        """Return the entire history"""
        return self.data

    def clear_history(self):
        """Clear the historical data"""
        self.data = []
        self.save_data()


if __name__ == "__main__":
    history = HistoryData()

   
    history.add_entry("User started a new session.")

  
    print("Current History Data:")
    for entry in history.get_history():
        print(f"{entry['timestamp']}: {entry['entry']}")



