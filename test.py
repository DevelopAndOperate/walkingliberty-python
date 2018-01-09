import walkingliberty
import re


def test_version():
    version = walkingliberty.__version__
    assert bool(re.match(r'^(\d+)\.(\d+)\.(\d+)$', version))


def test_address_determinism():
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.address('PotatoCancer541AlphaFartz') == '1MiD4qj3T668cPonjNYcYDzZSYTgHJvdiy'
    assert WalkingLiberty.address('satoshi') == '1xm4vFerV3pSgvBFkyzLgT1Ew3HQYrS1V'

    WalkingLibertyBCH = walkingliberty.WalkingLiberty(currency='BCH')
    assert WalkingLibertyBCH.address('PotatoCancer541AlphaFartz') == '1MiD4qj3T668cPonjNYcYDzZSYTgHJvdiy'
    assert WalkingLibertyBCH.address('satoshi') == '1xm4vFerV3pSgvBFkyzLgT1Ew3HQYrS1V'

    WalkingLibertyWIF = walkingliberty.WalkingLiberty(wallet_mode='wif')
    assert WalkingLibertyWIF.address('5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc') == '1coinNJHaeuAN5io49RtDfryxFLWnKR15'


def test_address_balance():
    """
    Should be zero unless someone sends to it.
    """
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.balance('ShouldTotallyBeZeroBalance') == 0
    assert WalkingLiberty.balance('PotatoCancer541AlphaFartz') == 0

    WalkingLibertyBCH = walkingliberty.WalkingLiberty(currency='BCH')
    assert WalkingLiberty.balance('ShouldTotallyBeZeroBalance') == 0

    WalkingLibertyWIF = walkingliberty.WalkingLiberty(wallet_mode='wif')
    # This WIF is for an uncompressed address.
    assert WalkingLibertyWIF.balance('5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc') == 2000
