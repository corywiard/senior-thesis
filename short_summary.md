Short Summary:

I am sharing my code, DataCollection.py, with you. I have commented out in the  
main function most of the methods. The only methods that are needed to be looked
at are def dataCollectorReds(year): and def data_store_csv_Reds(year, names_dict_reds):.
The first method is dataCollectorReds where I collect the data. Line 29-32 creates
a list that stores the variable names. Line 38-44 creates a list for all the names
of the players stores them and turns the list into a dictionary. Lines 47-50
collects all of the players data. The order it collects the data is by each player,
it collects each players data all the way through and then onto the next. Line
53-61 is a multi-dimensional list. This list first stores the variables in the first
index. Then a while loop is run for the length of the names. While this runs it
adds 0-17 index of data_row list into multi-dimensional list. This stores each of
the players data into different index of lists. Line 64-66 runs a for loop into
the dictionary storing each of the players data with their name. This gets put into
data_store_csv_Reds where it takes the dictionary to a csv. The df = df.transpose()
flips the csv form into a wrong format where the name is not correct and other data
is shifted. If you remove this line then you get the original csv I sent to you.
