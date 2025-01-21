import re
from collections import defaultdict

def parse_logs(log_file, threshold=5):
    """
    Dive into the log file and sniff out failed login attempts. If an IP screws up enough times,
    we’re calling them out. 

    Parameters:
        log_file (str): File path to the logs. You know, where all the drama is stored.
        threshold (int): Number of mess-ups before we get suspicious. Default is 5.

    Returns:
        dict: A dictionary where the keys are the shady IPs and the values are their fail counts.
    """
    suspicious_ips = defaultdict(int)  # This is our tally sheet for bad behavior.

    # Think of this pattern as a treasure map for hunting IPs in the logs.
    login_failure_pattern = r"Failed password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)"

    try:
        # Cracking open the log file like it's a mystery novel.
        with open(log_file, 'r') as file:
            for line in file:
                # We’re looking for lines where someone bombed their login. Classic.
                match = re.search(login_failure_pattern, line)
                if match:
                    ip = match.group("ip")  # Found one! Grab the IP and start counting.
                    suspicious_ips[ip] += 1
    except FileNotFoundError:
        # Uh-oh. The log file doesn’t exist. Are you sure you put it in the right place?
        print(f"Error: File {log_file} not found. Did you lose it?")
        return {}
    except PermissionError:
        # Some files are off-limits. We’re just not that cool yet.
        print(f"Error: Can't read {log_file}. Permission issues? Try asking nicely.")
        return {}

    # Now we play favorites: only keep IPs that messed up enough times to get on our radar.
    return {ip: count for ip, count in suspicious_ips.items() if count >= threshold}

def generate_report(suspicious_ips):
    """
    Time to show off the results of our detective work. We’re making a list of shady IPs
    and their screw-ups.

    Parameters:
        suspicious_ips (dict): This is our hot list of IPs and how often they’ve been bad.
    """
    print("\n=== Suspicious IPs Report ===")
    if not suspicious_ips:
        # No suspects today. Maybe it’s a slow day for crime?
        print("No suspicious activity detected. Everyone’s behaving... for now.")
    else:
        # Okay, here’s the lineup of bad guys.
        for ip, count in suspicious_ips.items():
            print(f"IP: {ip}, Attempts: {count}")

# The big show starts here.
if __name__ == "__main__":
    log_file_path = "auth.log"  # This is where we’ll look for the juicy details.

    print("Analyzing logs...")  # Cue the detective music.
    suspicious_ips = parse_logs(log_file_path)

    if suspicious_ips:
        # Found some shady folks! Let’s expose them.
        print(f"Suspicious IPs detected: {list(suspicious_ips.keys())}")
    generate_report(suspicious_ips)

# python parse_logs.py to run script