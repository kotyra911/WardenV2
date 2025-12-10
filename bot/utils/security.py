import hashlib



def get_hash_value(combined_string):

    return hashlib.sha256(combined_string.encode()).hexdigest()