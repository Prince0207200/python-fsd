import re
from collections import deque, defaultdict

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

recent_logs = deque(maxlen=3)
user_dict= defaultdict(list)
level_dict = defaultdict(int)


# Add a log
def add_log(line:str) -> None:
    arr=line.split()

    user=arr[2]
    user=user[:len(user)-1]
    level=arr[1]
    user_dict[user].append(level)
    level_dict[level] += 1
    recent_logs.append(line)

add_log(logs[0])

print(list(recent_logs))
print(dict(user_dict))
print(dict(level_dict))

