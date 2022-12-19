from json import JSONEncoder

class FighterJSONENCODER(JSONEncoder):
        def default(self, obj):
                return obj.__dict__ 