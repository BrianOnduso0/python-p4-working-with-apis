import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.json()  # Parse JSON directly into Python dictionary

    def program_agencies(self):
        programs_list = []
        programs = self.get_programs()
        for program in programs:
            if "agency" in program:  # Check if 'agency' key exists in the program dictionary
                programs_list.append(program["agency"])

        return programs_list

# Instantiate GetPrograms class
programs = GetPrograms()

# Get the list of agencies
agencies = programs.program_agencies()

# Print each agency (removing duplicates with set)
for agency in set(agencies):
    print(agency)
