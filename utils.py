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


def rand_n_digits(num_digits):
    """ Generates a random integer with n digits """
    range_start = 10**(num_digits-1)
    range_end = (10**num_digits) - 1
    return random.randint(range_start, range_end)


def start_enable_service(service):
    """ Starts and enables a service """
    cmdlist = ['systemctl', 'start', service]
    simple_popen(cmdlist)

    cmdlist = ['systemctl', 'enable', service]
    simple_popen(cmdlist)


def stop_disable_service(service):
    """ Stops and disables a service """
    cmdlist = ['systemctl', 'stop', service]
    simple_popen(cmdlist)

    cmdlist = ['systemctl', 'disable', service]
    simple_popen(cmdlist)


def set_masquerade():
    """ Sets firewall to masquerade on public zone """
    cmdlist = ['firewall-cmd', '--zone=public', '--add-masquerade']
    simple_popen(cmdlist)


def set_firewall(port):
    """ Given a port, open it on public interface """
    port_str = '--add-port=%s/tcp' % str(port)
    cmdlist = ['firewall-cmd', '--zone=public', port_str]
    simple_popen(cmdlist)


def remove_firewall(port):
    """ Given a port, remove it on public interface """
    port_str = '--remove-port=%s/tcp' % str(port)
    cmdlist = ['firewall-cmd', '--zone=public', port_str]
    simple_popen(cmdlist)
