"""
WalkingLiberty

Sort of a Bitcoin wallet API
"""

from urllib2 import urlopen

import pybitcoin
import yaml
import jsonrpclib

VALID_APIS = ('external', 'electrum')
VALID_CURRENCIES = ('BTC',)
# BCH in progress, needs work on pybitcoin
# VALID_CURRENCIES = ('BTC', 'BCH')
VALID_WALLET_MODES = ('deterministic-type1', 'wif')

DEFAULT_API = VALID_APIS[0]
DEFAULT_CURRENCY = VALID_CURRENCIES[0]
DEFAULT_WALLET_MODE = VALID_WALLET_MODES[0]

# This should be dynamic eventually.
# As of 2017-06-02, to confirm in 1 day you need about 43k Satoshis.
# 30k should put us notably under a week.
# 10k Satoshis is two weeks and counting, so not sustainable.
EXTERNAL_DEFAULT_FEE = 30000


class WalkingLiberty():
    """
    WalkingLiberty class.
    """
    def __init__(self,
                 api=None,
                 api_endpoint=None,
                 currency=None,
                 wallet_mode=None):
        # # We do this strange thing because if a caller sets None, we won't
        #  override it otherwise which will cause a needless failure.
        if api is None:
            api = DEFAULT_API

        if currency is None:
            currency = DEFAULT_CURRENCY

        if wallet_mode is None:
            wallet_mode = DEFAULT_WALLET_MODE
        # #

        if api not in VALID_APIS:
            message = 'api must be one of: {}'.format(VALID_APIS)
            raise ValueError(message)

        if currency not in VALID_CURRENCIES:
            message = 'currency must be one of: {}'.format(VALID_CURRENCIES)
            raise ValueError(message)

        if wallet_mode not in VALID_WALLET_MODES:
            message = 'wallet_mode must be one of: {}' \
                      ''.format(VALID_WALLET_MODES)

        if api == 'external' and currency != 'BTC':
            message = 'Cannot use external API and non-BTC currency.'
            raise ValueError(message)

        if api == 'electrum' and api_endpoint is None:
            message = 'With api of "electrum", api_endpoint must be set.'
            raise ValueError(message)

        if api == 'external' and api_endpoint is not None:
            message = 'With api of "external", api_endpoint must not be set.'
            raise ValueError(message)

        self.api = api
        self.api_endpoint = api_endpoint
        self.currency = currency
        self.wallet_mode = wallet_mode

    def _private_key(self, private_key):
        """
        Returns a private key object
        """
        if self.wallet_mode == 'deterministic-type1':
            BPK = pybitcoin.BitcoinPrivateKey
            return BPK.from_passphrase(passphrase=private_key)
        elif self.wallet_mode == 'wif':
            return pybitcoin.BitcoinPrivateKey(private_key)

    def address(self, private_key):
        """
        Returns address for key
        """
        return self._private_key(private_key).public_key().address()

    def balance(self, private_key):
        """
        Returns balance for a private key's address.
        """
        pub_address = self.address(private_key)

        if self.api == 'external':
            ADDRESS_API = 'https://bitaps.com/api/address/{}'
            data = urlopen(ADDRESS_API.format(pub_address)).read()
            dictionary = yaml.safe_load(data)
            # This is already in Satoshis.
            return dictionary['balance']
        elif self.api == 'electrum':
            # FIXME: Move to pybitcoin?
            electrum_server = jsonrpclib.Server(self.api_endpoint)
            balances = electrum_server.getaddressbalance(pub_address)
            total_balance = float(balances['confirmed'])
            total_balance += float(balances['unconfirmed'])
            satoshi_balance = int(total_balance * 100000000)
            return satoshi_balance

    def send(self, private_key, address, satoshis, fee=None):
        """
        Sends amount to address from the private_key's wallet.
        """
        if self.api == 'external':
            client = pybitcoin.BlockcypherClient()
        elif self.api == 'electrum':
            client = pybitcoin.ElectrumClient(api_endpoint=self.api_endpoint)
        priv_key = self._private_key(private_key)
        # FIXME: Add fee estimation. Will require some support on
        # pybitcoin's end.
        if fee is None:
            fee = EXTERNAL_DEFAULT_FEE
        return pybitcoin.send_to_address(address,
                                         satoshis,
                                         priv_key,
                                         client,
                                         fee=fee)
