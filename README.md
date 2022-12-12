# csv-filter-challenge-public
# Instructions
1. Click "Use this template" to create a copy of this repository in your personal github account.  
1. Using technology of your choice, complete assignment listed below (we use [GoLang](https://go.dev/) at Scoir, so if you know Go, show it off, but that's not required!).
1. Update the README in your new repo with:
    * a `How-To` section containing any instructions needed to execute your program.
    * an `Assumptions` section containing documentation on any assumptions made while interpreting the requirements.
1. Send an email to Scoir (sbeyers@scoir.com and msullivan@scoir.com) with a link to your newly created repo containing the completed exercise (preferably no later than one day before your interview).

## Expectations
1. This exercise is meant to drive a conversation. 
1. Please invest only enough time needed to demonstrate your approach to problem solving, code design, etc.
1. Within reason, treat your solution as if it would become a production system.

## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

## How-To
   1. To execute this program, first clone the repo and then from the command line run the command `python3 main.py`
   2. The user will then be prompted to pick a field (first_name, last_name, or dob) to filter the csv file by
   3. The user will then be prompted to enter a value that will be searched within the chosen column from step 2
   4. If any results are found, they will be printed to the console

## Assumptions
   - The file to be used with this program, will be the "test.csv" file

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```
