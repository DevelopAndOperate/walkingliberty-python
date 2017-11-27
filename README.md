# Walking Liberty: Python 2
## Try to make Bitcoin payments as easy as spending a Walking Liberty.

By default, uses a single-address deterministic type 1 wallet. Can use a single-address wif as well.

You have to use `--process-depdency-links` with `pip` for the time being: https://github.com/pypa/pip/issues/4187

```
pip install walkingliberty --process-dependency-links


# Get address for 'satoshi'
walkingliberty address satoshi

# Get balance for 'satoshi'
walkingliberty balance satoshi

# Get balance for '5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc'
walkingliberty --wallet_mode wif 5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc balance

# Send 10,000 Satoshis from 'potato' to 1address
walkingliberty send potato 1address 10000
```

Note that your phrase is likely to show up in ps output, which can be a security risk. You can control /proc access on Linux (and the equivalent systems calls on FreeBSD) with the right mount options or sysctl tunables. Probably a wise idea, anyway.

# Licence

[Unlicense/Public domain](LICENSE.txt)
