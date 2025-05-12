import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def reduction_function(hash_hex, step, length=10):
    x = int(hash_hex, 16)
    mod = 26 ** length
    S = (x + step) % mod
    password = []
    for _ in range(length):
        password.append(chr(97 + (S % 26)))
        S = S // 26
    return ''.join(reversed(password))


def build_chain(start_password, chain_length=16):
    chain = []
    current_pwd = start_password
    chain.append(current_pwd)

    for step in range(1, chain_length):
        current_hash = hash_password(current_pwd)
        chain.append(current_hash)
        current_pwd = reduction_function(current_hash, step)
        chain.append(current_pwd)
    return chain


def crack_password(target_hash, chains):
    for chain in chains:
        if target_hash in chain:
            idx = chain.index(target_hash)
            return chain[idx - 1]
    return None


if __name__ == "__main__":
    initial_passwords = [
        "vilniusgeo",
        "begisbegis",
        "vytautaslt",
        "palangageo",
        "zarasaigeo"
    ]


    chains = [build_chain(pwd, 8) for pwd in initial_passwords]

    for i, chain in enumerate(chains):
        print(f"\nChain {i +1} ({initial_passwords[i]}):")
        for j, item in enumerate(chain):
            if j % 2 == 0:
                print(f"  p{j // 2 + 1}: {item}")
            else:
                print(f"  h{j // 2 + 1}: {item}")


    target_hash = "299116273e0fcfba60917311a51dda2d"
    cracked = crack_password(target_hash, chains)

    if cracked:
        print(f"\n✅ Found! Password: {cracked}")
    else:
        print("\n❌ Not found")
