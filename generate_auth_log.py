import random

def generate_auth_log(file_name, num_entries=50):
    """
    Generate a mock authentication log with random entries.

    Parameters:
        file_name (str): Name of the file to save the logs.
        num_entries (int): Number of log entries to generate.
    """
    with open(file_name, 'w') as file:
        ips = ["192.168.1.101", "10.0.0.42", "172.16.0.23", "203.0.113.5", "8.8.8.8"]
        actions = [
            "Failed password for invalid user testuser from {ip} port 22 ssh2",
            "Accepted password for validuser from {ip} port 22 ssh2",
            "Failed password for root from {ip} port 22 ssh2",
            "Connection closed by invalid user {ip} port 22",
        ]

        for _ in range(num_entries):
            ip = random.choice(ips)
            action = random.choice(actions).format(ip=ip)
            file.write(action + "\n")

# Generate the mock log file
generate_auth_log("auth.log", num_entries=100)
print("Mock auth.log file created!")
