# Walking Liberty: Python 3
## Try to make Bitcoin/Bitcoin Cash payments as easy as spending a Walking Liberty.

## **Breaking change**:

WalkingLiberty 0.1.X used uncompressed addresses. WalkingLibery 0.2+ uses compressed addresses. This means that if you upgrade you will not see or have access to funds in existing wallets. `--fee` is gone (at least for the time being), however fee estimation should be much better now.

Also, WalkingLiberty 0.2+ is Python 3 only. 0.1.X was Python 2 only, so you will need to switch from pip to pip3 (quite likely). 0.2+ switches from [pybitcoin](https://github.com/blockstack/pybitcoin) to [bit](https://github.com/ofek/bit) and [bitcash](https://github.com/sporestack/bitcash) (for [Bitcoin Cash](https://www.bitcoincash.org/)).

This is a very rough change but the compressed addresses will bring about lower fees. bit is also a much superior library and actively maintained.

### Migrating from an uncompressed to compressed address

Verify your balance: `walkingliberty balance YOURWALKINGLIBERTYPHRASE`

Upgrade from WalkingLibery 0.1.X to 0.2+: `pip uninstall walkingliberty; pip3 install walkingliberty`

Verify 0 balance on the compressed address: `walkingliberty balnce YOURWALKINGLIBERTYPHRASE` (Yes, it really should be 0)

Grab the uncompressed WIF key: `python2 -c "import pybitcoin; print(pybitcoin.BitcoinPrivateKey.from_passphrase('YOURWALKINGLIBERTYPHRASE').to_wif())"`

Grab your new compressed address: `walkingliberty address YOURWALKINGLIBERTYPHRASE`

Sweep the funds from the uncompressed address into the compressed address: `walkingliberty --wallet_mode wif sweep 5JTUGMm2wQAHd7PM9msMVsT2Rz3NuBneRVanPXxDKN3RQjQm3ee 12XRjmGMbnkAesG9cTCnGETUnjvpg55Nws`

Verify your balance: `walkingliberty balance YOURWALKINGLIBERTYPHRASE` (Should be the same as it once was, minus TX fees)

And of course, this software is provided **without warranty**. Use it at your own peril. Read the source code, understand what it does, consult with experts, etc. If you use it incorrectly or there's a bug and you lose your magic internet money, the author(s) are not liable.

## Usage

By default, uses a single-address deterministic type 1 wallet. Can use a single-address wif as well.

```
pip3 install walkingliberty


# Get address for 'satoshi'
walkingliberty address satoshi

# Get balance for 'satoshi'
walkingliberty balance satoshi

# Get balance for '5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc'
walkingliberty --wallet_mode wif 5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc balance

# Send 10,000 Satoshis from 'potato' to 1address
walkingliberty send potato 1address 10000

# If you want to work with Bitcoin Cash, use --currency with all calls. For example:
walkinglibery --currency BCH balance satoshi
walkingliberty --currency BCH send potato 1address 10000
# etc
```

Note that your phrase is likely to show up in ps output, which can be a security risk. You can control /proc access on Linux (and the equivalent systems calls on FreeBSD) with the right mount options or sysctl tunables. Probably a wise idea, anyway.

# Licence

[Unlicense/Public domain](LICENSE.txt)
