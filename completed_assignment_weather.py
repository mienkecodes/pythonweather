import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"








def convert_date(iso_string):

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Parse the ISO string into a datetime object
    date_object = datetime.fromisoformat(iso_string)

    # Define lists for weekday and month names
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Extract individual components from the datetime object
    weekday = weekdays[date_object.weekday()]
    day = str(date_object.day)
    #fixing the days that only show as 4 rather than 04
    if len(day)<2:
        day="0"+day #if length less than 2 add 0
    month = months[date_object.month - 1]  # Month values are 1-based
    year = str(date_object.year)

    # Construct the human-readable date format
    formatted_date = f"{weekday} {day} {month} {year}"

    # Return the formatted date
    return formatted_date


#ALTERNATIVE
    # date_object = datetime.fromisoformat(iso_string)  # Parse the ISO string into a datetime object

    # formatted_date = date_object.strftime("%A %d %B %Y")  # Format the date using strftime

    # return formatted_date








def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    temp_in_celsius = (float(temp_in_farenheit) - 32) * 5 / 9
    return round(temp_in_celsius, 1)












def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
# Initialize variables for sum and count
    total = 0
    count = 0

    # Iterate through the elements in weather_data
    for value in weather_data:
        # Check if the value is numeric
        if isinstance(value, (int, float)):
            # Add the numeric value to the sum
            total += value
            # Increment the count
            count += 1
        else:
            # Try converting the value to a numeric type
            try:
                numeric_value = float(value)
                # Add the numeric value to the sum
                total += numeric_value
                # Increment the count
                count += 1
            except ValueError:
                # Skip non-numeric values
                pass

    # Calculate the mean by dividing the sum by the count
    mean = total / count if count != 0 else 0

    # Return the mean value
    return mean











def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []  # Initialize an empty list to store the data

    with open(csv_file, 'r') as file:  # Open the csv file in read mode
        reader = csv.reader(file)  # Create a csv reader object

        next(reader, None)  # Skip the header row

        for row in reader:  # Iterate over each row in the csv file
            if row:  # Check if the row is not empty
                row[1] = int(row[1])  # Convert the second column to an integer
                row[2] = int(row[2])  # Convert the third column to an integer
                data.append(row)  # Append the row to the data list

    return data  # Return the final list of data












def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """


    # Check if the list is empty
    # Check if the list is empty
    if not weather_data:
        return ()

    # Convert the elements in the list to floats
    new_list = []
    for number in weather_data:
        new_list.append(float(number))

    # Find the minimum value and its index
    min_value = min(new_list)
    min_index = new_list.index(min_value)

    # Build a list of all indices with the minimum value
    min_index_list = []
    index_counter = 0

    for number in new_list:
        if min_value == number:
            min_index_list.append(index_counter)
        index_counter += 1

    # Return the minimum value and the last index in the list
    return min_value, min_index_list[-1]










def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if not weather_data:
        return ()
    

    # Check if the list is empty
    if not weather_data:
        return ()

    # Convert the elements in the list to floats
    new_list = []
    for number in weather_data:
        new_list.append(float(number))

    # Find the maximum value and its index
    max_value = max(new_list)
    max_index = new_list.index(max_value)

    # Build a list of all indices with the maximum value
    max_index_list = []
    index_counter = 0

    for number in new_list:
        if max_value == number:
            max_index_list.append(index_counter)
        index_counter += 1

    # Return the maximum value and the last index in the list
    return max_value, max_index_list[-1]








def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    if not weather_data:
        return "No weather data available."
    
# create empty lists
    temp_min_list = []
    temp_max_list = []
    date_list = []

# Iterate over each line in weather_data and extract the relevant data
    for line in weather_data:
        date_list.append(line[0])  # Store the date in the date_list
        temp_min_list.append(line[1])  # Store the minimum temperature in the temp_min_list
        temp_max_list.append(line[2])  # Store the maximum temperature in the temp_max_list

# Find the minimum and maximum temperatures and their corresponding positions in the lists
    min_value_f = find_min(temp_min_list)[0]  # Find the minimum value in temp_min_list in Fahrenheit
    min_value_c = convert_f_to_c(min_value_f)  # Convert the minimum value to Celsius
    min_data_position = find_min(temp_min_list)[1]  # Find the position of the minimum value in temp_min_list
    max_value_f = find_max(temp_max_list)[0]  # Find the maximum value in temp_max_list in Fahrenheit
    max_value_c = convert_f_to_c(max_value_f)  # Convert the maximum value to Celsius
    max_data_position = find_max(temp_max_list)[1]  # Find the position of the maximum value in temp_max_list

# Calculate the average low and high temperatures in Fahrenheit and convert them to Celsius
    average_low_f = calculate_mean(temp_min_list)  # Calculate the average of temp_min_list in Fahrenheit
    average_low_c = convert_f_to_c(average_low_f)  # Convert the average low temperature to Celsius
    average_high_f = calculate_mean(temp_max_list)  # Calculate the average of temp_max_list in Fahrenheit
    average_high_c = convert_f_to_c(average_high_f)  # Convert the average high temperature to Celsius

# Construct the summary string in the desired format using the calculated values
    return (
    f"{len(weather_data)} Day Overview\n"
    f"  The lowest temperature will be {format_temperature(min_value_c)}, and will occur on {convert_date(date_list[min_data_position])}.\n"
    f"  The highest temperature will be {format_temperature(max_value_c)}, and will occur on {convert_date(date_list[max_data_position])}.\n"
    f"  The average low this week is {format_temperature(average_low_c)}.\n"
    f"  The average high this week is {format_temperature(average_high_c)}.\n"
)

#test
example_one_given = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
    ]

print(generate_summary(example_one_given))








    



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No weather data available."


# Initialize an empty string to store the summary
    summary = ""  

# Iterate over each entry in weather_data
    for entry in weather_data:
        date = entry[0]  # Extract the date from the entry
        max_temp = convert_f_to_c(round(entry[2], 1))  # Convert and round the maximum temperature to Celsius
        min_temp = convert_f_to_c(round(entry[1], 1))  # Convert and round the minimum temperature to Celsius
        day = date.split("T")[0].split("-")[2]  # Extract the day from the date
        month = date.split("T")[0].split("-")[1]  # Extract the month from the date
        year = date.split("T")[0].split("-")[0]  # Extract the year from the date
# Adding data to the summary
        summary += f"---- {convert_date(entry[0])} ----\n"  # Add the formatted date to the summary
        summary += f"  Minimum Temperature: {min_temp}°C\n"  # Add the minimum temperature to the summary
        summary += f"  Maximum Temperature: {max_temp}°C\n\n"  # Add the maximum temperature to the summary

    return summary  # Return the final summary string


#testing on screen
example_one = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

print(generate_daily_summary(example_one))






