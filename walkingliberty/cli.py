"""
WalkingLiberty CLI
"""

import argparse

import walkingliberty

def address(args):
    print(walkingliberty.address(args.phrase))


def balance(args):
    print(walkingliberty.balance(args.phrase))


def send(args):
    print(walkingliberty.send(args.phrase,
                              args.address,
                              args.satoshis,
                              args.fee))

def main():
    parser = argparse.ArgumentParser(description='WalkingLiberty CLI.')

    subparser = parser.add_subparsers()
    address_subparser = subparser.add_parser('address',
                                             help='Returns address corresponding with phrase.')
    address_subparser.set_defaults(func=address)
    address_subparser.add_argument('phrase', help='Deterministic phrase.')

    balance_subparser = subparser.add_parser('balance',
                                             help='Returns balance corresponding with phrase.')
    balance_subparser.set_defaults(func=balance)
    balance_subparser.add_argument('phrase', help='Deterministic phrase.')

    send_subparser = subparser.add_parser('send',
                                          help='Sends Bitcoin.',
                                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    send_subparser.set_defaults(func=send)
    send_subparser.add_argument('phrase', help='Deterministic phrase.')
    send_subparser.add_argument('address', help='Address to send to.')
    send_subparser.add_argument('satoshis', help='Satoshis to send.', type=int)
    send_subparser.add_argument('--fee', help='Transaction fee.', type=int, default=walkingliberty.FEE)

    args = parser.parse_args()
    # This calls the function or wrapper function, depending on what we set
    # above.
    args.func(args)


if __name__ == '__main__':
    main()
