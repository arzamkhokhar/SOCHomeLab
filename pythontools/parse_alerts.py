import json

INPUT_FILE = "/home/vboxuser/sample_alerts.json"

def find_key(d, target_key):
    if isinstance(d, dict):
        if target_key in d:
            return d[target_key]
        for value in d.values():
            result = find_key(value, target_key)
            if result is not None:
                return result
    elif isinstance(d, list):
        for item in d:
            result = find_key(item, target_key)
            if result is not None:
                return result
    return None

failed_logins = {}
total_alerts = 0

with open(INPUT_FILE, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            alert = json.loads(line)
        except json.JSONDecodeError:
            continue

        total_alerts += 1
        rule_id = alert.get("rule", {}).get("id", "")

        if rule_id == "60122":
            user = find_key(alert, "targetUserName") or "unknown"
            failed_logins[user] = failed_logins.get(user, 0) + 1

print(f"Total alerts scanned: {total_alerts}")
print(f"Failed login counts by user:")
for user, count in failed_logins.items():
    print(f"  {user}: {count}")

import csv
with open("/home/vboxuser/failed_login_report.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Username", "Failed Login Count"])
    for user, count in failed_logins.items():
        writer.writerow([user, count])

print("Report saved to failed_login_report.csv")
