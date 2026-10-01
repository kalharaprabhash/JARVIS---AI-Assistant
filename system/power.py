import subprocess


def lock_pc():
    subprocess.run(
        "rundll32.exe user32.dll,LockWorkStation"
    )


def shutdown_pc():
    subprocess.run(
        "shutdown /s /t 10"
    )


def cancel_shutdown():
    subprocess.run(
        "shutdown /a"
    )


def restart_pc():
    subprocess.run(
        "shutdown /r /t 10"
    )


def sleep_pc():
    subprocess.run(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )