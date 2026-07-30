import sys
import re

# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     pattern = r"INFO \((.+)\)$"
#     result = re.search(pattern, line)
#     if result:
#       print(result[1])

def show_time_of_pid(line):
  pattern = r"^(\w+ \d \d+:\d+:\d+).+\[(\d{5})\]"
  result = re.search(pattern, line)
  return result[1] + " pid:" + result[2] if result else None

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


#creating a dictionary of usernames and their counts
logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)