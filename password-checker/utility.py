import requests
def get_apidata(urlApi,query_char):
    url = f'{urlApi}{query_char}' 
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status.code}')
    return res


def get_leakpassword_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash,count in hashes:
        if hash_to_check == hash:
            return count
    return 0
