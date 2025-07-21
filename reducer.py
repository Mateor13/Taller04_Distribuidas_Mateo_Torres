import os

user_datetimes = {}

for file in os.listdir("splits"):
    if file.endswith(".out"):
        with open(f"splits/{file}", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(' ', 2)
                    if len(parts) >= 3:
                        user = parts[0]
                        count = int(parts[1])
                        datetimes_part = parts[2].strip('[]')
                        
                        if user not in user_datetimes:
                            user_datetimes[user] = []
                        
                        if datetimes_part:
                            datetimes = datetimes_part.split(',')
                            user_datetimes[user].extend(datetimes)
 
with open("reporte.txt", 'w') as report:
    for user, all_datetimes in user_datetimes.items():
        unique_datetimes = sorted(list(set(all_datetimes)))
        total_count = len(unique_datetimes)
        datetimes_str = ','.join(unique_datetimes)
        line = f"{user} {total_count} [{datetimes_str}]\n"
        report.write(line)