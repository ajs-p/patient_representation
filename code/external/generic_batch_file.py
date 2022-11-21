# from
# https://github.com/lhncbc/skr_web_python_api/blob/main/examples/generic_batch_file.py

import argparse
from skr_web_api import Submission, BATCH_VALIDATION_URL, CAS_SERVERURL


def unescape_string(textstring):
    """Remove leading backslashes from text string"""
    return textstring.replace('\\', '')

if __name__ == '__main__':
    serverurl = f"{CAS_SERVERURL}/tickets"
    tgtserverurl = f"{CAS_SERVERURL}/api-key"
    serviceurl = BATCH_VALIDATION_URL
    parser = argparse.ArgumentParser(description="test cas auth")
    parser.add_argument('-e', '--email', help='Email address')
    parser.add_argument('-a', '--apikey', help='UTS api key')
    parser.add_argument('-c', '--cmd', default='metamap',
                        help='batch command')
    parser.add_argument('-r', '--cmdargs',
                        default='-E -I',
                        help='batch command arguments')
    parser.add_argument('inputfile', help='inputfile')
    parser.add_argument('-s', '--serviceurl',
                        default=serviceurl,
                        help='url of service')
    args = parser.parse_args()

    print("cmd: {}".format(args.cmd))
    print("cmdargs: {}".format(unescape_string(args.cmdargs)))
    inst = Submission(args.email, args.apikey)
    if args.serviceurl:
        inst.set_serviceurl(args.serviceurl)
    inst.init_generic_batch(args.cmd, unescape_string(args.cmdargs))
    inst.set_batch_file(args.inputfile)
    response = inst.submit()
    print('response status: {}'.format(response.status_code))
    print('content: {}'.format(response.content.decode()))