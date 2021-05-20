# Data Manipulator
Data Manipulator is a tool that collects, organizes, and stores data on up to
12 National League Major League Baseball teams.

## Key Features

* Automatically collects data on 12 different MLB teams in the National League
* Allows the user to select if 1 or all of teams get collected along with what years to collect for
* Organizes the data for each teams total data at the end of each season based on user selection

## Installing Data Manipulator Tool Unix/macOS/Windows:
To install Data Manipulator, use the commands:
check python3 version:
```
python3 --version
```

If python3 does not exist then install python3 on steps provided at:
```
https://www.python.org/
```

check pip installation:
```
python -m pip --version
```

pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4
downloaded from python.org

install pandas:
```
pip install pandas
```

install BeautifulSoup:
```
pip install beautifulsoup4
```

# Running Data Manipulator Tool Unix/macOS:
To create bash script:
```
chmod utx run.sh
```

To run both programs:
```
./run.sh
```

# Running Data Manipulator Tool Windows:
To run programs in terminal:
```
python3 DataCollection.py
python3 DataOrganizer.py
```

Another option would be to create a batch file using the .bat extension.
Steps:
```
1. Create the batch file, open notepad
2. In notepad have the following:
"Path where your Python exe is stored\python.exe" "Path where your Python script
is stored\script name.py"
pause

The first set of "" should be your path file to python.exe
The second set of "" should be path file to pyhon programs
3. Save notepad with .bat extension
4. Run the batch file
```

# R programing language
install R: https://www.r-project.org/

The file Regression.r holds the correct code to run multiple linear regressions
for all 12 teams. In order for the user to use this program some changes will
need to be made. Lines 2-3 can stay the same. The lines that will need changed
are:
`5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49`

These lines read in the CSV files for each of teams. It currently holds my path
to do that. Therefore, any user should implement their path in between the "" for
it to work. Once the proper path is implemented it can be ran.
To run the R program:
```
Rscript Regression.r
```
This will display each of the regressions in the terminal. The file `Graph.r` is
the graphs created in chapter 4 of my senior thesis. To replicate these graphs
change lines 7-18 to include the users path to the files in the "".
