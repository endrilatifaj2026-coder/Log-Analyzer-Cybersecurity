# Log Analyzer (Cybersecurity + Data Analysis)

This project is a Python-based log analyzer that detects suspicious login activity and identifies potential brute-force attacks.

## 🔍 Features
- Parses system log files
- Detects failed login attempts
- Identifies suspicious IP addresses
- Classifies risk levels (Medium / High)
- Generates reports
- Visualizes attack patterns using graphs

## 🛠️ Technologies Used
- Python
- Matplotlib

## 📊 Example Output
- Detects IPs with multiple failed login attempts
- Generates a report file
- Displays a bar chart of attack frequency

## ▶️ How to Run

1. Install dependencies:pip install -r requirements.txt

2. Run the analyzer:python analyzer.py

## 📁 Project Structure
- analyzer.py → main script
- log.txt → sample log data
- report.txt → generated output
- requirements.txt → dependencies

## 🧠 What I Learned
- Log parsing and analysis
- Cybersecurity fundamentals (brute-force detection)
- Data visualization
- Writing clean and structured Python code