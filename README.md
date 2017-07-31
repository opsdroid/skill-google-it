# opsdroid skill hello

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to respond with a google search link.

## Requirements

None.

## Configuration

```yaml
- name: google-it
  # Optional
  engine-url: https://www.google.co.uk/  # Url of the search engine you want to use
  query-arg: search?q=  # The uri for the search (default is for google)
```

## Usage

#### `google pomodoro technique`

Googles "pomodoro technique".

> user: google pomodoro technique
>
> opsdroid: https://www.google.co.uk/search?q=pomodoro+technique

## License

GNU General Public License Version 3 (GPLv3)
