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

## Deployment
* Requirements
    * Local computer with docker & docker-compose installed

1. Clone this repo to local workspace
1. From the working directory run docker-compose up
1. The image will be built and activated, database is populated via fixtures so can take a minuet or more to load depending on local hardware
1. The terminal will give you IP and port to access project, remember /word to call the API

## Technologies
* Docker
* Docker-compose
* Django
* Django-Rest-Framework

### Acknowledgements

[Matthewreagan on github for a JSON version of the Websters English dictionary.](https://github.com/matthewreagan/WebstersEnglishDictionary)