# https://github.com/lhncbc/skr_web_python_api/blob/main/examples/mm_interactive.py

""" MetaMap interactive using embedded string """
import argparse
from skr_web_api import Submission, METAMAP_INTERACTIVE_URL

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="test cas auth")
    parser.add_argument('-s', '--serviceurl',
                        default=METAMAP_INTERACTIVE_URL,
                        help='url of service')
    parser.add_argument('-e', '--email', help='Email address')
    parser.add_argument('-a', '--apikey', help='UTS api key')
    parser.add_argument('-i', '--input', help='Input string to pass to METAMAP')
    parser.add_argument('-p', '--params', default='-I --JSONn --negex --conj', 
                                        help='param string to pass to METAMAP')
    args = parser.parse_args()
    inputtext = args.input
    inst = Submission(args.email, args.apikey)
    if args.serviceurl:
        inst.set_serviceurl(args.serviceurl)
    # inst.init_mm_interactive(inputtext, args='-N') 
    inst.init_mm_interactive(inputtext, args=args.params)
    response = inst.submit()
    print('response status: {}'.format(response.status_code))
    print('content: {}'.format(response.content.decode()))