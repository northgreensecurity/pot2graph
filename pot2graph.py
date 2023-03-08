import csv
import re
import matplotlib.pyplot as plt

#Author: Dan Cannon (https://www.linkedin.com/in/daniel-cannon-75421130/)
#Company: North Green Security (www.northgreensecurity.com)
#Note: So far this will only analyse the data in your potfile, if you have any errors make sure there are no blank lines

print("\033[34m                                                                  &             \033[0m")
print("\033[34m                                          &&&%              &&&&&&&&&&&&        \033[0m")
print("\033[34m                                   &&&    &&&%             &&&         &&&      \033[0m")
print("\033[34m &&&&&&&&&&   &&&&&&&&&&  &&&&&&& &&&&&&  &&&&&&&&&&      &&&    \033[32m///\033[0m\033[34m    &&&     \033[0m")
print("\033[34m &&&    *&&& &&&&    &&&% &&&&     &&&    &&&&    &&&   &&&&&   \033[32m///\033[0m\033[34m     &&/     \033[0m")
print("\033[34m &&&     &&&  &&&    &&&  &&&&     &&&    &&&%    &&&    &&&   \033[32m///\033[0m\033[34m     &&&      \033[0m")
print("\033[34m &&&     &&&   &&&&&&&&   &&&&      &&&&  &&&%    &&&         \033[32m///\033[0m\033[34m     &&&   \033[32m////\033[0m\033[34m  \033[0m")
print("\033[32m                                                             \033[32m///\033[0m\033[34m     &&&   \033[32m/////\033[0m\033[34m  \033[0m")
print("\033[32m ///////////  /////// //////////  /////////   //////////     \033[32m///\033[0m\033[34m    &&&    \033[32m///  \033[0m")
print("\033[32m////    ////  ////    ////////// ///////////  ///    ////    \033[32m///\033[0m\033[34m    &     \033[32m///   \033[0m")
print("\033[32m ///*   ////  ///     ///    ///  ///   ////  ///    ////     \033[32m///\033[0m        \033[32m///    \033[0m")
print("\033[32m  //////////  ///       //////     ///////    ///    ////       \033[32m//////////\033[0m      \033[0m")
print("\033[32m ///    ////                                                                    \033[0m")
print("\033[32m  ////////   \033[0m")

print("\n")
print("Pot2Graph\nA visualisation tool for cracked passwords")
print("\n")


# Ask user for Potfile
potfile_name = input("Please enter the name of the potfile to be analysed: ")

# Open Potfile
with open(potfile_name, "r") as f:
    potfile = f.readlines()


# Create a dictionary to store the data
data = {}

# Iterate through the potfile
for line in potfile:
    # Split the line into the hash and password
    hash, password = line.strip().split(":")
    length = len(password)
    if length in data:
        data[length] += 1
    else:
        data[length] = 1

# Create the pie chart
labels = list(data.keys())
sizes = list(data.values())
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Distribution of Password Lengths in Potfile")
plt.savefig("potfile_graph.jpg")
plt.show()

# Write the data to a CSV file
with open("potfile_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Length", "Count"])
    for key, value in data.items():
        writer.writerow([key, value])

