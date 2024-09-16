import hashlib


# write by codeium
def hashfile(file: str):
    sha256 = hashlib.sha256()
    with open(file, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


print(hashfile("hash.py"))
print(hashfile("hashfile.py"))
