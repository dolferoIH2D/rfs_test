import rsa

def generate_rsa_pair(size):
    """
        Generates new pair of RSA keys and returns dict with them.
    """
    (pubkey, privkey) = rsa.newkeys(size)
    keys = {
        'public_key': str(pubkey),
        'private_key': str(privkey),
    }
    return keys
