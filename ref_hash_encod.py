class MarsURLEncoder:

    def __init__(self):
        self.ref_cod_dict = {}
    

    def encode(self, long_url):
        import hashlib

        md5_hash = hashlib.new('md5')
        md5_hash.update(long_url.encode())
        md5_hex = md5_hash.hexdigest()
        if md5_hex not in self.ref_cod_dict:
            self.ref_cod_dict[md5_hex] = long_url
        else:
            md5_hash = hashlib.new('md5')
            md5_hash.update(long_url.encode())
            md5_hex = md5_hash.hexdigest()
            self.ref_cod_dict[md5_hex] = long_url
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        return 'https://ma.rs/' + md5_hex

    def decode(self, short_url):
        hash_tag = short_url[len('https://ma.rs/'):]
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        long_url = self.ref_cod_dict[hash_tag]
        return long_url

mu = MarsURLEncoder()
print(mu.encode('https://www.rbc.ru/'))
print(mu.decode(mu.encode('https://www.rbc.ru/')))

