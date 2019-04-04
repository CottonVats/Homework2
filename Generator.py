import hashlib
def file_hash(path):
    with open(path, 'rb') as file:
        while True:
            strip = file.readline()
            if not strip:
                break
            yield hashlib.md5(strip).digest()
