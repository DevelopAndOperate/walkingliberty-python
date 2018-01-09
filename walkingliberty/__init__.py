"""
WalkingLiberty

Sort of a Bitcoin and Bitcoin Cash wallet API
"""

from hashlib import sha256

import bit
import bitcash

__version__ = '0.2.0'

VALID_CURRENCIES = ('btc', 'bch')
VALID_WALLET_MODES = ('deterministic-type1', 'wif')

DEFAULT_CURRENCY = VALID_CURRENCIES[0]
DEFAULT_WALLET_MODE = VALID_WALLET_MODES[0]


class WalkingLiberty():
    """
    WalkingLiberty class.
    """
    def __init__(self,
                 currency=None,
                 wallet_mode=None):
        # # We do this strange thing because if a caller sets None, we won't
        #  override it otherwise which will cause a needless failure.
        if currency is None:
            currency = DEFAULT_CURRENCY

        if wallet_mode is None:
            wallet_mode = DEFAULT_WALLET_MODE
        # #

        if currency not in VALID_CURRENCIES:
            message = 'currency must be one of: {}'.format(VALID_CURRENCIES)
            raise ValueError(message)

        if wallet_mode not in VALID_WALLET_MODES:
            message = 'wallet_mode must be one of: {}' \
                      ''.format(VALID_WALLET_MODES)

        if currency == 'btc':
            self.bit = bit
        elif currency == 'bch':
            self.bit = bitcash

        self.currency = currency
        self.wallet_mode = wallet_mode

    def _private_key(self, private_key):
        """
        Returns a private key object
        """
        # sha256() wants bytes, Key() wants a string.
        if self.wallet_mode == 'deterministic-type1':
            private_key = bytes(private_key, 'utf-8')
            return self.bit.Key.from_hex(sha256(private_key).hexdigest())
        elif self.wallet_mode == 'wif':
            return self.bit.Key(private_key)

    def address(self, private_key):
        """
        Returns address for key
        """
        private_key = self._private_key(private_key)
        return private_key.address

    def balance(self, private_key, unit='satoshi'):
        """
        Returns balance for a private key's address.

        Optionally, set unit for desired unit. (satoshi, btc, usd, etc)
        """
        private_key = self._private_key(private_key)
        # Doesn't always return as an int from Bit. :-/
        return int(private_key.get_balance(currency=unit))

    def send(self, private_key, address, satoshis, unit='satoshi'):
        """
        Sends amount to address from the private_key's wallet.
        """
        private_key = self._private_key(private_key)
        outputs = [(address, satoshis, unit)]
        # Have to call get_unspents() or get_balance() before send()
        private_key.get_unspents()
        return private_key.send(outputs, combine=False)

    def sweep(self, private_key, address):
        """
        Sweeps all coins from private_key into address.
        """
        private_key = self._private_key(private_key)
        private_key.get_unspents()
        return private_key.send([], combine=True, leftover=address)
