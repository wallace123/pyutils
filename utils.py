""" Utility functions to be used in other Python scripts """
import subprocess
import random


def simple_popen(cmdlist):
    """ Wrapper for subprocess.Popen function. Provide
        shell commands in list form.
    """
    proc = subprocess.Popen(cmdlist,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    output, errors = proc.communicate()

    return output, errors


def change_file(thefile, old, new):
    """ Opens a file, reads the contents, replaces old text with new text,
        writes out the new file
    """
    with open(thefile, 'r') as fil:
        contents = fil.read()
        fil.close()

    # Check if new already exists in contents so we don't double replace when script
    # is rerun.
    if new not in contents:
        contents = contents.replace(old, new)

        with open(thefile, 'w') as fil:
            fil.write(contents)
            fil.close()


def create_loop_devices(loops):
    """ Creates 'loops' number of loop devices in /dev """

    with open('/etc/modules-load.d/loop.conf', 'w') as loop_conf:
        loop_conf.write('loop')
        loop_conf.close()

    with open('/etc/modprobe.d/loop_options.conf', 'w') as loop_options:
        loop_options.write('options loop max_loop=%d' % loops)
        loop_options.close()

    simple_popen(['rmmod', 'loop'])
    simple_popen(['modprobe', 'loop'])


def rand_N_digits(n):
    """ Generates a random integer with n digits """
    range_start = 10**(n-1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)
