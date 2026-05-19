import winreg

def scan_bam():

    results = []

    path = r"SYSTEM\CurrentControlSet\Services\bam\State\UserSettings"

    try:

        reg = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            path
        )

        for i in range(winreg.QueryInfoKey(reg)[0]):

            sid = winreg.EnumKey(reg, i)

            results.append({
                "file": sid,
                "modified": "BAM Registry Entry"
            })

    except Exception as e:

        results.append({
            "file": str(e),
            "modified": "Registry Error"
        })

    return results
