import urllib.parse

from opsdroid.matchers import match_regex


@match_regex(r'^(?:google|search) (.*)')
async def hello(opsdroid, config, message):
    search_term = urllib.parse.quote_plus(message.regex.group(1))
    engine_url = config.get("engine-url", "https://www.google.co.uk/")
    query_arg = config.get("query-arg", "search?q=")
    await message.respond("Here's what I found {}{}{}".format(engine_url, query_arg, search_term))
