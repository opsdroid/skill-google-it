# opsdroid skill google it

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to respond with a google search link.

## Requirements

None.

## Configuration

```yaml
skills:
  - name: google-it
    # Use Google search engine (Default)
    engine-url: https://www.google.co.uk/
    query-arg: search?q=
    # Other search engines that can be used (keep only one uncommented at a time)
    # Use Bing search engine
#   engine-url: https://www.bing.com/
#   query-arg: search?=
    # Use DuckDuckGo search engine
#   engine-url: https://duckduckgo.com/
#   query-arg: ?q=
    # Use Yahoo search engine
#   engine-url: http://search.yahoo.com/
#   query-arg: search?p=
    # Use Aol search engine
#   engine-url: https://search.aol.co.uk/aol/
#   query-arg: search?query=
    # Use Ask search engine
#   engine-url: https://uk.ask.com/
#   query-arg: web?q=
    # Use Wolframalpha search engine
#   engine-url: https://www.wolframalpha.com/input/
#   query-arg: ?i=
```

## Usage

#### `google pomodoro technique`

Googles "pomodoro technique".

> user: google pomodoro technique
>
> opsdroid: https://www.google.co.uk/search?q=pomodoro+technique
