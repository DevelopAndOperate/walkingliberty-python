"""
WalkingLiberty CLI
"""

import argparse

import pyqrcode

import walkingliberty


def address(args):
    WalkingLiberty = walkingliberty.WalkingLiberty(args.api,
                                                   args.api_endpoint,
                                                   args.currency,
                                                   args.wallet_mode)
    address = WalkingLiberty.address(args.phrase)
    if args.qr is True:
        qr = pyqrcode.create(address)
        print(qr.terminal(module_color='black',
                          background='white',
                          quiet_zone=1))
    print(address)


def balance(args):
    WalkingLiberty = walkingliberty.WalkingLiberty(args.api,
                                                   args.api_endpoint,
                                                   args.currency,
                                                   args.wallet_mode)
    print(WalkingLiberty.balance(args.phrase))


def send(args):
    WalkingLiberty = walkingliberty.WalkingLiberty(args.api,
                                                   args.api_endpoint,
                                                   args.currency,
                                                   args.wallet_mode)
    print(WalkingLiberty.send(args.phrase,
                              args.address,
                              args.satoshis,
                              args.fee))


def main():
    parser = argparse.ArgumentParser(description='WalkingLiberty CLI.')
    parser.add_argument('--api', help='API', default=None)
    parser.add_argument('--api_endpoint', help='API endpoint', default=None)
    parser.add_argument('--currency', help='Currency', default=None)
    parser.add_argument('--wallet_mode', help='Wallet mode', default=None)

    subparser = parser.add_subparsers()
    address_subparser = subparser.add_parser('address',
                                             help="Returns phrase's address.")
    address_subparser.set_defaults(func=address)
    address_subparser.add_argument('phrase', help='Deterministic phrase.')
    address_subparser.add_argument('--qr',
                                   help='QR code',
                                   action='store_true',
                                   default=False)

    balance_subparser = subparser.add_parser('balance',
                                             help="Returns phrase's balance.")
    balance_subparser.set_defaults(func=balance)
    balance_subparser.add_argument('phrase', help='Deterministic phrase.')

    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    send_subparser = subparser.add_parser('send',
                                          help='Sends Bitcoin.',
                                          formatter_class=formatter_class)
    send_subparser.set_defaults(func=send)
    help = 'Deterministic phrase.'
    send_subparser.add_argument('phrase', help=help)
    help = 'Address to send to.'
    send_subparser.add_argument('address', help=help)
    help = 'Satoshis to send'
    send_subparser.add_argument('satoshis', help=help, type=int)
    help = 'Transaction fee.'
    send_subparser.add_argument('--fee', help=help, type=int, default=None)

    args = parser.parse_args()
    # This calls the function or wrapper function, depending on what we set
    # above.
    args.func(args)


if __name__ == '__main__':
    main()
