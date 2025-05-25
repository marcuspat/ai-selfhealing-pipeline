"""
Parses a log file and extracts lines with common failure patterns.
This simulates the first step in self-healing: issue detection.
"""

def parse_log_file(file_path):
    keywords = ["ERROR", "FAILURE", "Timeout", "Crash", "Refused", "Unavailable"]
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        issues = [line.strip() for line in lines if any(k in line for k in keywords)]
        return issues
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []

if __name__ == "__main__":
    file_path = input("Enter log file path: ")
    results = parse_log_file(file_path)
    if results:
        print("\n⚠️  Detected issues:")
        for line in results:
            print(f" - {line}")
    else:
        print("✅ No known issues detected.")
