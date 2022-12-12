import sys
import csv

fields = {
    "first_name": 0,
    "last_name": 1,
    "dob": 2
}

def main():
    input_field_prompt = "Choose a field to view (first_name, last_name, dob) (press 'q' to quit): \n"
    user_input_field = input(input_field_prompt).lower()

    # Allows user to press 'q' to quit
    while(user_input_field != "q"):

        # If field name is invalid, ask for field name again
        while(user_input_field not in fields):
            user_input_field = input("Please insert valid field name (first_name, last_name, or dob):\n")
        
        # Search for value in column specified by user input
        user_input_key = input("Enter {} to search:\n".format(user_input_field)).lower()
        search_csv("test.csv", user_input_field, user_input_key)
        found_records = search_csv("test.csv", user_input_field, user_input_key)

        # Display results
        if (len(found_records) != 0):
            print("\nResults:")
            for record in found_records:
                print(",".join(record))
            print("\n")
        else:
            print("No records could be found in {}".format("test.csv"))
        
        # Prompt user for input again
        user_input_field = input("Choose a field (first_name, last_name, or dob) to view (press 'q' to quit):\n")



def search_csv(file_name, field, key):
    """
        Parameters:
            - file_name(str): name of csv file
            - field(str): csv column to be searched (first_name, last_name, etc.)
            - key(str): Value that is being searched wihin column
    """
    results = []
    try:
        file = open(file_name)
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row[fields[field]].lower() == key:
                results.append(row)
    except:
        print("{} could not be opened".format(file_name))
    finally:
        return results


if __name__ == "__main__":
    main()