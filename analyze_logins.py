from collections import defaultdict
import re

log_file = "logs/django_app.log"  # log faylingiz manzili
threshold = 3  # Nechta urinishdan keyin ogohlantirish

ip_attempts = defaultdict(int)

with open(log_file, "r") as f:
    for line in f:
        if "LOGIN ATTEMPT" in line:
            match = re.search(r'IP=(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

print("❗ Ko‘p marta login urinish qilgan IP manzillar:")
for ip, count in ip_attempts.items():
    if count >= threshold:
        print(f"{ip} - {count} ta urinish")
