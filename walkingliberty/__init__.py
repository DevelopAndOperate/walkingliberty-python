"""
WalkingLiberty

Sort of a Bitcoin wallet API
"""

from urllib2 import urlopen

import pybitcoin
import yaml

WALLETAPI = 'https://bitaps.com/api/address/{}'


def _phrase_to_key(phrase):
    """
    Returns a private key from a phrase.
    """
    return pybitcoin.BitcoinPrivateKey.from_passphrase(passphrase=phrase)


def address(phrase):
    """
    Returns address for key
    """
    return _phrase_to_key(phrase).public_key().address()


def balance(phrase):
    """
    Returns balance for a phrase's address.
    """
    pub_address = address(phrase)
    data = urlopen(WALLETAPI.format(pub_address)).read()
    dictionary = yaml.safe_load(data)
    return dictionary['balance']


def send(phrase, address, satoshis):
    """
    Sends amount to address from the phrase wallet.
    """
    client = pybitcoin.BlockchainInfoClient()
    priv_key = _phrase_to_key(phrase)
    return pybitcoin.send_to_address(address, satoshis, priv_key, client)
