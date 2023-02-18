import os
import socket
from collections import Counter

Counter = Counter()

def my_ip_address():
    # Get the IP address of your computer
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def count_words_in_file(file):
    # Count the number of words in a text file, and update a counter with the word counts
    total_word_count = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                cleaned_line = line.replace("Â", "")
                words = cleaned_line.split()
                if file.name.endswith("IF.txt"):
                    Counter.update(words)
                total_word_count += len(words)
    return total_word_count

text_files_word_counts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")   #remove result file if exists previously
output_string="Text file at location: /home/data \n"
for each_file in os.listdir(path):
    if each_file.endswith(".txt"):
        output_string=output_string+each_file+"\n"
        text_files_word_counts[each_file] = count_words_in_file(path + "/" + each_file)
        
output_string=output_string+"\n"
output_string=output_string+"Read the two text files and count total number of words in each text file \n"
all_files_wordcount = 0
all_files_names = ""
for each_key in text_files_word_counts.keys():
    all_files_names = all_files_names + each_key + ","
    all_files_wordcount = all_files_wordcount + text_files_word_counts.get(each_key)
    output_string = output_string +"Total number of words in [" + each_key + "] is : " + str(text_files_word_counts.get(each_key))+"\n"

output_string = output_string +"\n"
output_string = output_string +"Grand Total \n"
output_string = output_string +"Total number of words in both files [" + all_files_names[0:len(all_files_names) - 1] + "] is: " + str(all_files_wordcount)+"\n"

output_string = output_string +"\n"
output_string = output_string +"Top Three words with maximum number of counts in IF.txt \n"
output_string = output_string +str(Counter.most_common(3))+"\n"

output_string = output_string +"\n"
output_string = output_string +"IP address \n"
output_string = output_string +"Your Computer IP Address is:" + my_ip_address()

results_textfile = open(path + "/" +"result.txt","w")
results_textfile.write(output_string)
results_textfile.close()
for each_line in open(path + "/" +"result.txt","r").readlines():
    print(each_line.replace("\n",""))
