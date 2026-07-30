import subprocess
import os
subprocess.run(["date"])

subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)



result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True)

print(result.returncode)

print(result.stdout)

print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

print(result.stdout)
print(result.stderr)



my_env = os.environ.copy() #Creates a copy of the current env variables
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]]) #this adds a new path to the copy of the PATH variable

result = subprocess.run(["myapp"], env=my_env) #we run the command with the modified environment variables