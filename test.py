import walkingliberty


def test_address_determinism():
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.address('PotatoCancer541AlphaFartz') == '171JAQEE1uEUji5ex9hx1K9mpwcEcj86yd'
    assert WalkingLiberty.address('satoshi') == '1ADJqstUMBB5zFquWg19UqZ7Zc6ePCpzLE'


def test_address_balance():
    """
    Should be zero unless someone sends to it.
    """
    WalkingLiberty = walkingliberty.WalkingLiberty()
    assert WalkingLiberty.balance('ShouldTotallyBeZeroBalance') == 0
    assert WalkingLiberty.balance('PotatoCancer541AlphaFartz') == 2000
