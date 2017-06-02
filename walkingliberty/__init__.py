"""
WalkingLiberty

Sort of a Bitcoin wallet API
"""

from urllib2 import urlopen

import pybitcoin
import yaml

# This should be dynamic eventually.
# As of 2017-06-02, to confirm in 1 day you need about 43k Satoshis.
# 30k should put us notably under a week.
# 10k Satoshis is two weeks and counting, so not sustainable.
FEE = 30000

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
    client = pybitcoin.BlockcypherClient()
    priv_key = _phrase_to_key(phrase)
    return pybitcoin.send_to_address(address,
                                     satoshis,
                                     priv_key,
                                     client,
                                     fee=FEE)
