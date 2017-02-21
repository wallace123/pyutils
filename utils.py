""" Utility functions to be used in other Python scripts """
import subprocess


def simple_popen(cmdlist):
    """ Wrapper for subprocess.Popen function. Provide
        shell commands in list form.
    """
    proc = subprocess.Popen(cmdlist,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    output, errors = proc.communicate()

    return output, errors
