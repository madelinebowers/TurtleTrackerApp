#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Madeline Bowers (meb158@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Ask the user for a date, specifying the format
user_date = "7/3/2003" #input("Enter a date (M/D/YYYY): ")

#Create a variable point to the data file
file_name = './data/raw/Sara.txt.txt'

#Create a file object from the filename
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#close the file object
file_object.close()

#Create empty dictionaries
date_dict = {}
location_dict = {}

#Extract one data line into a variable
for lineString in line_list:
    
    #check to see if the lineString is a data line
    if lineString[0] in ('#', 'u'):
            continue
    
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split() 
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    obs_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
        
    #Add items to dictionaries if lc criteria is met
    if obs_lc in ("1","2","3"):
        date_dict [record_id] = obs_date
        location_dict [record_id] = (obs_lat, obs_lon)
        
    # Print information to the user
    print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
