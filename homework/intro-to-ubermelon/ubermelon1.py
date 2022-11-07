log_file = open("um-server-01.txt")  #sets variable to open log file 1


def generate_sales_reports(log_file):  #funtion to generate sales report for Monday
    for line in log_file:  #loop through Monday's report
        line = line.rstrip()  #removes white space at end of string:
        day = line[0:3]  #creates variable, day, to index 0-2
        if day == "Mon":  #if variable, day, is Monday
            print(line)  #print the data from that line


generate_sales_reports(log_file)  #calls funtion generate_sales_reports