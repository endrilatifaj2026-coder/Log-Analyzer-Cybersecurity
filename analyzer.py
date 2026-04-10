def analyze_logs(filename):
    failed_count = {}

    with open(filename, "r") as file:
        for line in file:
            if "failed" in line:
                parts = line.split(" ")
                ip = parts[0]

                failed_count[ip] = failed_count.get(ip, 0) + 1

    return failed_count


def show_alerts(data):
    print("\n--- Suspicious Activity ---")

    for ip, count in data.items():
        if count > 1:
            print(f"ALERT: {ip} -> {count} failed attempts")

def analyze_logs(filename):
    failed_count = {}

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")

            if len(parts) == 3:
                timestamp, ip, action = parts

                if "failed" in action:
                    failed_count[ip] = failed_count.get(ip, 0) + 1

    return failed_count

def analyze_logs(filename):
    failed_count = {}

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")

            if len(parts) == 3:
                timestamp, ip, action = parts

                if "failed" in action:
                    failed_count[ip] = failed_count.get(ip, 0) + 1

    return failed_count


def detect_bruteforce(data):
    print("\n--- Brute Force Detection ---")

    for ip, count in data.items():
        if count >= 3:
            print(f"⚠️ HIGH RISK: {ip} -> {count} failed attempts")
        elif count == 2:
            print(f"⚠️ MEDIUM RISK: {ip} -> {count} failed attempts")


data = analyze_logs("log.txt")
detect_bruteforce(data)


data = analyze_logs("log.txt")
show_alerts(data)

def save_results(data):
    with open("report.txt", "w") as file:
        for ip, count in data.items():
            file.write(f"{ip} -> {count} failed attempts\n")


save_results(data)
import matplotlib.pyplot as plt

def plot_data(data):
    ips = list(data.keys())
    counts = list(data.values())

    plt.bar(ips, counts)
    plt.xlabel("IP Address")
    plt.ylabel("Failed Attempts")
    plt.title("Failed Login Attempts by IP")

    plt.show()


plot_data(data)