from subprocess import CalledProcessError, STDOUT, check_output, call


def getoutput(cmd):
    try:
        data = check_output(cmd, shell=True, stderr=STDOUT)
    except CalledProcessError as ex:
        data = ex.output
    if data[-1:] == '\n':
        data = data[:-1]
    return data


def run(cmd):
    return call(cmd, shell=True)
