# 09/02/2019 - Jackline Atsango
# Python Prerequisites Summative Assessment


### Problem 1 - Generate a dummy dataset ###

import random

objects = [n for n in range(1,33,1)]; # list comprehension to generate sensor list

ones = [1] * 16;

sensorObject = {};  # data will be stored in a dictionary

for i in objects:   # for loop to populate the dictionary with sensor list and random set of floats
    
    sensorObject[i] = [ round(random.random(), 3) * n for n in ones];   # rounding to 3 decimal places 
    
    
# Alter the dummy data to contain corrupted entries --- for problem 3

sensorObject[8] = [0,0.1,0,0,'err',0,0,0,0.2,0,0,0,0,'err',0,0];
sensorObject[32] = ['err', 0,0,0,'err',0,0,0,'err',0,0,0,0,0,0,0];


### Problem 2 - Store the generated data with each iteration ###

import datetime

with open('sensor_data.txt', 'a') as outputFile:
    
    t = datetime.datetime.now()         # create time stamp for each iteration
    t.strftime('%Y-%m-%d')
    
    outputFile.write(str(t) + ',' + '\n')
    
    for value in sensorObject.values():    
        
        for element in value:           # store each number, without the '[]' list characters
            
            outputFile.write(str(element) + ',')
            
        outputFile.write('\n')          # seperate each 'value' with a new line, output as follows:
                                       
        
### Problem 3 - function to test for string entries in the data ###
 
# This function will read the sensor data and validate the points, search for 'err', store in a log if an error is found and the # date of the iteration where the was an error
# The function returns a dictionary

# In future -- 1. Function should evaluate for more than 'err', in case of other corruptions
#              2. Function should convert the input back to float, except for corrupted or error points

def validateData(sensorData):
    
    t = sensorData[0].strip('\n');         # extract and store the date
    
    del sensorData[0];                     # remove the date entry from the readings
    
    for idx, value in enumerate(dataObject.values()):   # loop to remove characters and check for errors ('err')
        
        value = value.split(',')           # split the value string into a list
        
        for count, reading in enumerate(value):
            
            if reading == '\n':            # remove end of line character
                
                value.pop(count)
               
            if reading == 'err':           # log any errors found
                
                with open('error_log.txt', 'a') as errorOutput:   # write to a log file
                
                    errorOutput.write(str(t) + ' error in sensor {} reading {} \n'.format(idx, (count))) 
     
        sensorData[idx + 1] = value;            # dictionary with sensor 1 - 32
        
    return sensorData;
        
        
## Read the stored sensor data - This section can be convereted into a function in future, with the file name as an input

with open('sensor_data.txt', 'r') as inputFile:
    
    data = inputFile.readlines()

# Assuming there will only be 32 entries + 1 datestamp, therefore 33 entries

logs = len(data) / 33;       # To determine the number of iterations of readings

sensorReadings = {};         # This will be a dictionary of dictionaries, containing all the logs in a sensor file

for entry in range(logs):       # for each iteration of readings 
    
    index = (entry + 1) * 33;   # Start and index calculate the range of data points and at which line to start
    
    start = entry * 33;
    
    count = 0;                  # start from 0 for each iteration and instatiate a new dictionary
    
    dataObject = {};
    
    for line in range(start, index):
                        
        dataObject[count] = data[line];
        
        count += 1
            
    sensorReadings[entry] = dataObject;
    
## Call the function on the data

validatedInput = {};

validatedInput = validateData(sensorReadings[0]);  # Looking only at the first reading for example but can be looped through

#print(validatedInput)  # FYI for the output format  