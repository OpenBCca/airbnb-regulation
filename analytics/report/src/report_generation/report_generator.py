print("Starting script...")
#import pandas as pd
import os
from jinja2 import Environment, FileSystemLoader

# Sample data
data = {
    "listing_id": [1, 2, 3, 4, 5, 6, 7],
    "address": ["11 ABC street.", "22 ABC street.", "33 ABC street.", "44  ABC street.", "55  ABC street.", "66  ABC street.", "77  ABC street."],
    "policy_A": [True, False, True, False, True, False, True]
}


########################################################################
########################################################################
# USING JINJA2 TO HTML
########################################################################
########################################################################


# Get the absolute path to the directory containing report_generator.py
dir_path = os.path.dirname(os.path.realpath(__file__))

# Use this path to set the correct path to the template/ directory
template_dir = os.path.join(dir_path, 'template')


# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('reporttemplate.html')

# get the date of report generation as the current date
from datetime import datetime
today = datetime.now()
todayStr = today.strftime('%Y-%m-%d %H:%M')

# render the template with the data
html_out = template.render(
    data=data,
    date=todayStr
)

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the output file
output_file = os.path.join(script_dir, '../report_store/output.html')

# Write the HTML table to the output file
print("Writing HTML table to output.html...")
with open(output_file, 'w') as f:
    f.write(html_out)

print("Done!")


########################################################################
########################################################################
# USING DATAFRAME TO HTML
########################################################################
########################################################################


# # Convert the array to a DataFrame
# df = pd.DataFrame(data)
# print("Converted data to DataFrame")

# # Convert the DataFrame to an HTML table
# html_table = df.to_html(index=False)
# print("Converted DataFrame to HTML table")

# # Get the absolute path to the directory containing the script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct the absolute path to the output file
# output_file = os.path.join(script_dir, '../report_store/output.html')


# # Write the HTML table to the output file
# print("Writing HTML table to output.html...")
# with open(output_file, 'w') as f:
#     f.write(html_table)

# print("Done!")