from collections import defaultdict
import string
import random
class Codec:
    def __init__(self):
        self.sup_chars = []
        self.map = {}
        self.sup_chars.extend(list(string.ascii_letters))
        self.sup_chars.extend(list(string.digits))
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        """
        def gen_url():
            while True:
                turl = list("http://tinyurl.com/")
                for i in range(6):
                    turl.append(random.choice(self.sup_chars))
                url = ''.join(turl)
                if not self.map.get(url, None):
                    break
            return url
        turl = gen_url()
        self.map[turl] = longUrl
        return turl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        """
        return self.map.get(shortUrl, None)

if __name__ == '__main__':
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    print(url)
    enc = codec.encode(url)
    print(enc)
    print(codec.decode(enc))