# Python program to convert
# JSON file to CSV
 
 
import json
import csv
 
for i in range(0,14):
    # Opening JSON file and loading the data
    # into the variable data
    with open('data/endsong_'+str(i)+'.json') as json_file:
        data = json.load(json_file)
 
    streaming_data = data
 
    # now we will open a file for writing
    data_file = open('data/endsong_'+str(i)+'.csv', 'w')
 
    # create the csv writer object
    csv_writer = csv.writer(data_file)
 
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
 
    for song in streaming_data:
        if count == 0:
     
            # Writing headers of CSV file
            header = song.keys()
            csv_writer.writerow(header)
            count += 1
 
        # Writing data of CSV file
        csv_writer.writerow(song.values())
 
    data_file.close()
