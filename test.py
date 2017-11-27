import walkingliberty


def test_address_determinism():
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.address('PotatoCancer541AlphaFartz') == '171JAQEE1uEUji5ex9hx1K9mpwcEcj86yd'
    assert WalkingLiberty.address('satoshi') == '1ADJqstUMBB5zFquWg19UqZ7Zc6ePCpzLE'

    WalkingLibertyWIF = walkingliberty.WalkingLiberty(wallet_mode='wif')
    assert WalkingLibertyWIF.address('5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc') == '1coinNJHaeuAN5io49RtDfryxFLWnKR15'


def test_address_balance():
    """
    Should be zero unless someone sends to it.
    """
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.balance('ShouldTotallyBeZeroBalance') == 0
    assert WalkingLiberty.balance('PotatoCancer541AlphaFartz') == 2000

    WalkingLibertyWIF = walkingliberty.WalkingLiberty(wallet_mode='wif')
    assert WalkingLibertyWIF.balance('5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc') == 2000
    assert WalkingLiberty.balance('5JN8q7UXFvsUTMuwePHxzd9byVGaeKvmMA6ZdV4fS4gYYiptMUc') == 0
