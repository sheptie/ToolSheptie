import os
import time

def search_ahk():

    results = []

    paths = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents")
    ]

    for path in paths:

        for root, dirs, files in os.walk(path):

            for file in files:

                if file.endswith(".ahk"):

                    full = os.path.join(root, file)

                    try:

                        modified = time.ctime(
                            os.path.getmtime(full)
                        )

                        results.append({
                            "file": full,
                            "modified": modified
                        })

                    except:
                        pass

    return results
