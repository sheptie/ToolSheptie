import os

SUSPICIOUS = [

    "clicker",
    "autoclick",
    "macro",
    "inject",
    "dll",
    "ghost",
    "cheat",
    "vape",
    "akira",
    "future",
    "entropy",
    "slinky",
    "rise",
    "sigma",
    "dope",
    "horion",
    "reach",
    "aimassist",
    "triggerbot",
    "velocity",
    "bhop",
    "16x16",
    "overlay"
]

def get_prefetch():

    folder = r"C:\Windows\Prefetch"

    results = []

    if not os.path.exists(folder):
        return results

    try:

        files = os.listdir(folder)

    except:
        return results

    for file in files:

        if not file.endswith(".pf"):
            continue

        lower = file.lower()

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

            "name": file,

            "status": status,

            "flags": ", ".join(found)
            if found else "None",

            "path": os.path.join(
                folder,
                file
            )
        })

    results.sort(

        key=lambda x:
        0 if x["status"] == "Suspicious"
        else 1 if x["status"] == "Warning"
        else 2
    )

    return results
