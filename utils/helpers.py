import subprocess
import os

def open_tool(path):

    try:

        if os.path.exists(path):

            subprocess.Popen(
                [path],
                shell=True
            )

    except Exception as e:

        print(e)
