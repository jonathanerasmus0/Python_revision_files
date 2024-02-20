'''Dependencies for The Next Exercise.

Please install the dependecies for some of the utility functions to run

pip install -r requirements.txt

Exercise 05: How to update a CSV based file

In this exercise, execute a helper function we have written to write new content to a file.

python helper.py --task make-csv --file task_5.csv --rows 100

Try this with different number of rows so your program can take a longer time to run for example, 2000 rows.

Profile the CPU usage of your computer as you run the instructions below. Keep checking on the statistics to know if the computer can really handle all this load. In Linux (and Mac), the command top can be used in the terminal to determine the CPU usage as you run scripts below.'''



import csv

# Define the file paths
csv_file = 'customers.csv'
temp_file = 'temp_customers.csv'

# Function to update the name in the 1000th row
def update_name_in_csv(csv_file, row_index, new_name):
    # Open the original CSV file for reading and a temporary CSV file for writing
    with open(csv_file, 'r', newline='') as file, open(temp_file, 'w', newline='') as temp:
        reader = csv.reader(file)
        writer = csv.writer(temp)

        # Copy the contents of the original file to the temporary file
        for index, row in enumerate(reader):
            if index == row_index - 1:  # Adjusting for 0-based index
                # Update the name in the 1000th row
                row[0] = new_name
            writer.writerow(row)

    # Replace the original file with the temporary file
    import os
    os.replace(temp_file, csv_file)

# Update the name in the 1000th row
update_name_in_csv(csv_file, 1000, 'JONATHAN DAVIES')


'''PERSONAL EXPLANATION FOR REVISION :The selected code is a function that updates the name in a specific row of a CSV file. The function takes three arguments: the CSV file path, the row index (zero-based), and the new name.

The function uses the csv module to read the CSV file and write to a temporary file. It loops through each row in the CSV file, checking if the current row is the specified row index. If it is, the function updates the name in the row.

Finally, the function uses the os module to replace the original CSV file with the temporary file.

Overall, the code is performing a simple update to a CSV file by updating a specific row. '''