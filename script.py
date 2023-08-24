import os
import shutil

source_path = "PS C:\Users\adity\VS CODE PROJECTS\CS50P"

for filename in os.listdir(source_path):
    if os.path.isfile(os.path.join(source_path, filename)):
        extension = filename.split('.')[-1]
        destination_folder = os.path.join(source_path, extension)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(
            os.path.join(source_path, filename),
            os.path.join(destination_folder, filename)
        )