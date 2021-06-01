from pybitcoin import ExtPubKey


def test_extpubkey(generate_extpubkey):
    extpubkey = ExtPubKey(generate_extpubkey)
    assert str(extpubkey) == generate_extpubkey


def test_bad_extpubkey_raises_error(generate_extpubkey):
    extpubkey = generate_extpubkey
    # Change part of the key so that it fails the checksum
    extpubkey = extpubkey[:10] + 'abcd' + extpubkey[14:]
    assert len(extpubkey) == len(generate_extpubkey)
    assert str(extpubkey) != generate_extpubkey
