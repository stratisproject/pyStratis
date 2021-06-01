from pybitcoin import PubKey


def test_pubkey_uncompressed(generate_uncompressed_pubkey):
    pubkey = PubKey(generate_uncompressed_pubkey)
    assert len(pubkey.compressed()) == 66
    assert len(pubkey.uncompressed()) == 130
    assert pubkey.uncompressed() == generate_uncompressed_pubkey


def test_pubkey_compressed(generate_compressed_pubkey):
    pubkey = PubKey(generate_compressed_pubkey)
    assert len(pubkey.compressed()) == 66
    assert len(pubkey.uncompressed()) == 130
    assert pubkey.compressed() == generate_compressed_pubkey
