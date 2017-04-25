import walkingliberty


def test_address_determinism():
    assert walkingliberty.address('PotatoCancer541AlphaFartz') == '171JAQEE1uEUji5ex9hx1K9mpwcEcj86yd'
    assert walkingliberty.address('satoshi') == '1ADJqstUMBB5zFquWg19UqZ7Zc6ePCpzLE'


def test_address_balance():
    """
    This probably won't last for long...
    Can easily be "stolen".
    """
    assert walkingliberty.balance('PotatoCancer541AlphaFartz') == 36969
