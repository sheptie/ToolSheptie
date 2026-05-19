import os
import time

def scan_recycle():

    results = []

    recycle = r"C:\$Recycle.Bin"

    try:

        for root, dirs, files in os.walk(recycle):

            for file in files:

                full = os.path.join(root, file)

                try:

                    modified = time.ctime(
                        os.path.getmtime(full)
                    )

                    results.append({
                        "file": file,
                        "modified": modified
                    })

                except:
                    pass

    except:
        pass

    return results
