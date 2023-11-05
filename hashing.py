import hashlib
import os
def hash_with_salt(input_data):
 # Generate a random salt
 salt = os.urandom(16)
 # Concatenate the salt and input data
 data_to_hash = salt + input_data.encode()
 # Hash the concatenated data
 hash_object = hashlib.sha256(data_to_hash)
 hash_hex = hash_object.hexdigest()
 # Return the salt and hash as a tuple
 return salt, hash_hex
# Mask the data
input_data = 'sensitive_data'
salt, hashed_data = hash_with_salt(input_data)
print(f"Salt: {salt}")
print(f"Hashed Data: {hashed_data}")
