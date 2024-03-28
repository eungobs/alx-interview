0x03 Log Parsing

Overview
This project focuses on parsing and processing data streams in real-time using Python programming. The main task involves reading from standard input (stdin), handling data in a specific format, and computing metrics based on the input data. The goal is to develop a script that reads stdin line by line, computes metrics, and prints statistics after every 10 lines or upon a keyboard interruption (CTRL + C).

Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
PEP 8 style (version 1.7.x) should be followed
All files must be executable

Project Details
Tasks
Log parsing
Write a script that reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Print statistics after every 10 lines and/or a keyboard interruption (CTRL + C).
Metrics to compute:
Total file size
Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
Status codes should be printed in ascending order.
Additional Resources
Mock Technical Interview
Implementation
The project starts on Mar 25, 2024 6:00 AM and ends by Mar 29, 2024 6:00 AM.
The checker was released on Mar 26, 2024 6:00 AM.
An auto review will be launched at the deadline.
Instructions
Clone the GitHub repository: alx-interview
Navigate to the directory 0x03-log_parsing.
Execute the script 0-stats.py.
Input log data through stdin.
View computed metrics and statistics printed after every 10 lines or upon keyboard interruption.

./0-stats.py < input_log_data.txt

Elizabeth Eunice Ndzukule - GitHub User:eungobs

Acknowledgments
Python Documentation
Regular Expressions in Python
Signal Handling in Python
File I/O in Python
PEP 8 Style Guide
Stack Overflow
