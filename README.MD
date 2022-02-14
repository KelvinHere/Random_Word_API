# Random Word API

An API that returns a random word and its meaning from a dictionary.  Using Dockerized Django REST

## How to call the API
/word will return json containing a random word and its meaning.

For example `http://127.0.0.1:8000/word/`

Returned JSON structure below
```
{
    "id": 15218,
    "word": "cosmographic",
    "meaning": "Of or pertaining to cosmography."
}
```

## Technologies
* Docker
* Django
* Django Rest

### Acknowledgements

[Matthewreagan on github for a JSON version of the Websters English dictionary.](https://github.com/matthewreagan/WebstersEnglishDictionary)