import subprocess


# ==========================================================
# OPEN WINDOWS APPLICATION
# ==========================================================

def open_application(command):

    command = command.lower().strip()

    applications = {

        "calculator": "calc.exe",

        "calc": "calc.exe",

        "notepad": "notepad.exe",

        "paint": "mspaint.exe",

        "file explorer": "explorer.exe",

        "explorer": "explorer.exe",

        "command prompt": "cmd.exe",

        "cmd": "cmd.exe",

        "powershell": "powershell.exe",

        "task manager": "taskmgr.exe"
    }

    if command in applications:

        subprocess.Popen(
            applications[command]
        )

        return True

    return False


# ==========================================================
# OPEN CHROME
# ==========================================================

def open_chrome():

    try:

        subprocess.Popen(
            [
                "cmd",
                "/c",
                "start",
                "",
                "chrome"
            ],
            shell=True
        )

        return True

    except Exception as e:

        print("Chrome error:", e)

        return False