import psutil

SUSPICIOUS = [

    "autoclick",
    "clicker",
    "macro",
    "injector",
    "cheat",
    "engine",
    "overlay",
    "vape",
    "horion",
    "akira",
    "entropy",
    "future"
]

def get_processes():

    results = []

    for proc in psutil.process_iter():

        try:

            name = proc.name()

            lower = name.lower()

            found = []

            for word in SUSPICIOUS:

                if word in lower:
                    found.append(word)

            status = "Clean"

            if len(found) >= 1:
                status = "Warning"

            if len(found) >= 2:
                status = "Suspicious"

            results.append({

                "name": name,

                "status": status,

                "flags": ", ".join(found)
                if found else "None",

                "path": proc.exe()
            })

        except:
            pass

    results.sort(

        key=lambda x:
        0 if x["status"] == "Suspicious"
        else 1 if x["status"] == "Warning"
        else 2
    )

    return results
