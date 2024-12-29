import subprocess
from typing import Optional, List


def run_shell_cmd(
    cmd: str, cwd: Optional[str] = None, verbose: bool = True
) -> List[str]:
    """run a command in the shell using Popen

    Args:
        cmd (str): command to run
        cwd (Optional[str]): current working directory
        verbose (bool): whether to print stdout lines

    Returns:
        List[str]: stdout lines
    """
    stdout_holder = []
    if cwd:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=cwd)
    else:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in process.stdout:
        # Decode bytes to string and strip whitespace
        line_str = line.decode("utf-8").strip()
        if verbose:
            print(line_str)
        stdout_holder.append(line_str)
    returncode = process.wait()
    if returncode != 0:
        print(f"Command '{cmd}' failed with return code {returncode}")
    return stdout_holder
