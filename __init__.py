import urllib.parse

from opsdroid.matchers import match_regex

@match_regex(r'^google (.*)')
async def hello(opsdroid, config, message):
    search_term = urllib.parse.quote_plus(message.regex.group(1))
    google_url = config.get("engine-url", "https://www.google.co.uk/")
    query_arg = config.get("query-arg", "search?q=")
    await message.respond("{}{}{}".format(google_url, query_arg, search_term))
