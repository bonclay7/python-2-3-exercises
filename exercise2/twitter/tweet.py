import json


class Tweet:
    def __init__(self, raw):
        self.raw = raw

    def followers(self):
        return self.  raw['user']['followers_count']

    def __cmp__(self, other):
        return other.followers() - self.followers()

    def __str__(self):
        return '@{0} at {1}: '.format(
            self.raw['user']['screen_name'],
            self.raw['created_at']) + self.raw['text']
