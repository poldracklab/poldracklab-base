"""Utility functions

This module provides general utility functions, including
functions to run shell commands and download files.

The module contains the following functions:

- `run_shell_cmd`: Run a shell command and return the output
- `DownloadFile`: Download a file from a URL to a local filename

"""

import subprocess
from typing import Optional, List
import requests
import os
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter


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


# from http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
def DownloadFile(
    url: str,
    local_filename: str,
    connect_timeout: float = 10.0,
    chunk_size: int = 1024,
) -> None:
    """
    Download a file from a URL to a local filename

    Args:
        url (str): the URL to download from
        local_filename (str): the local filename to save the file to
    """

    if not os.path.exists(os.path.dirname(local_filename)):
        os.makedirs(os.path.dirname(local_filename))
    s = requests.Session()
    s.mount("http://", HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[500])))

    r = s.get(url=url, timeout=connect_timeout)

    with open(local_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
