# Incident Response Tool

## Overview
This project includes:
   a log generator (for mock purposes)
   a log analysis tool (designed for incident response tasks) 
   It identifies suspicious IP addresses (involved in brute force attacks by parsing authentication logs)

## Features
   **Log Generator:** Creates realistic authentication logs for testing
   **Log Parser:** Analyzes logs to detect brute force attempts based on a configurable threshold
   **Detailed Reports:** Outputs suspicious IPs and their failed login counts

## How to Use
 Generate a sample log file:
   ```bash
   python generate_auth_log.py

## Finally, run this in a bash terminal: python parse_logs.py

## Prerequisites
   Python 3.x
   Basic knowledge of terminal commands
## Technologies Used
   Python
   Regular Expressions
   File I/O
   Incident Response Concepts
## Future Enhancements
   Add support for multiple log formats
   Integrate IP reputation lookups
   Firewall that blocks attempts 5+


Thanks for looking at my code!!
  - Fernando Acosta
