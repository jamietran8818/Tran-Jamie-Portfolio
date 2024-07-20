# SQLite-Commands
This program utilizes SQLite commands to parse through a dataset. 

## Installation:
-Using Python in Jupyter Notebook import sqlite3

## Loading Data:
-Utilizing the sqlite3.connect() command, open the 'petsdb' dataset

-To confirm that the connection was sucessful use the is_open() function

## Code:
-From there we utilize the cursor() to excute our commands and iterate over the data

-In this specfic project COUNT, GROUP BY, WHERE, and JOIN were used to sort and parse through the data. 

## Example:
-In the first iteration I created a for loop to parse through the data and print the number of people we had in each age group

-To count the indiviuals in each age group I used 'SELECT count(*), age FROM persons' 

-To have the counted number of individuals per age group I added 'GROUP BY age'

-Finally to have this diplayed nicely I added a print function to have the following numbers inserted into a sentence. 

-All of this resulted in the following function:

      cursor = pets.cursor()
      for people, age in cursor.execute('SELECT count(*), age FROM persons GROUP BY age'):
          print('We have {} people aged {}'.format(people, age))
          
-With this output(the following is only displaying the first 5 rows of the output):

We have 2 people aged 5

We have 1 people aged 6

We have 1 people aged 7

We have 3 people aged 8

We have 1 people aged 9
