import sys
from collections import Counter

filename = sys.argv[1]
user_registrations = []

with open(filename, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3:
            date = parts[0]
            time = parts[1]
            user = parts[2].split(':')[1]
            
            hour = int(time.split(':')[0])
            
            if hour < 8 or hour >= 18:
                user_registrations.append(f"{user}:{date}_{time}")

counts = Counter(user_registrations)

user_data = {}
for user_datetime, count in counts.items():
    user, datetime = user_datetime.split(':', 1)
    if user not in user_data:
        user_data[user] = []
    user_data[user].append(datetime)

with open(f"{filename}.out", 'w') as out:
    for user, datetimes in user_data.items():
        count = len(datetimes)
        datetimes_str = ','.join(sorted(datetimes))
        out.write(f"{user} {count} [{datetimes_str}]\n")