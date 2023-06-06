import zlib

def compute_hash(message):
    # Compute the CRC32 hash value
    crc32_hash = zlib.crc32(message.encode('utf-8'))

    # Truncate the hash value to 16 bits
    truncated_hash = crc32_hash & 0xFFFF

    return truncated_hash

# Example usage
def run_hash_verification():
    original_message = input("Enter the original message: ")
    received_message = input("Enter the received message: ")

    original_hash = compute_hash(original_message)
    received_hash = compute_hash(received_message)

    print("Original Message Hash (16 bits):", original_hash)
    print("Received Message Hash (16 bits):", received_hash)

    if original_hash == received_hash:
        print("Message integrity verified. Hashes match.")
    else:
        print("Message integrity compromised. Hashes do not match.")

run_hash_verification()
