import os

current_directory = os.getcwd()
print("Current working directory: ", current_directory)


outputs = {}

outputs['current_directory'] = current_directory
outputs['files_and_directories'] = os.listdir()
outputs["path_value"] = os.environ.get("PATH")

print(outputs)

print(os.path)