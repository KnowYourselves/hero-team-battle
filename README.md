# Superhero Team Battle

**_With 💜, by Raúl Esteban_**

## Requirements

This project requires Python 3.10 and Poetry 1.2.

## Setup

Run `poetry install` to install the dependencies, then you need to create the `.env` file, you can use the `.env.example` as a base. The variables are as follows:

- SUPERHERO_API_BASE_URL: URL to the Superhero API
- SUPERHERO_API_KEY: API key for the Superhero API
- TEAM_SIZE: Team size, defaults to five
- HERO_AMOUNT: Amount of heroes provided by the Superhero API, defaults to 731
- MAILGUN_API_BASE_URL: URL to the Mailgun API
- MAILGUN_API_KEY: API key for the Mailgun API
- MAILGUN_SENDER: Email to be used as the Mailgun sender
- EMAIL_DESTINATION: Email to send the report to

Once this the environment variables are set, the project can be run with `python3 main.py`.

## Suppositions

During the making of this project the following suppositions where made:

1. The random coefficient for the filiation coefficient is set when a hero is instantiated
2. There can be repeated heroes between teams
3. The starting hero for a fight is selected randomly
4. The hero ids will be sequential starting from one to some number.

## Closing Thoughts

It was fun programming this. It was the first time I used pydantic, since I mainly work with Django and I have to say I loved it! At first I was a little confused, since this program required computed fields, which pydantic hasn't implemented well yet but I managed to make it work.

I can see why so many people love pydantic, seeing how clean the transformation from request response to model representation ended up being. I hope they sort out computed fields when V2 comes out though.

As for the end result, I'd say I'm happy. I think it could be refactored more, for example, I could extract a HeroBattle class from TeamBattle, or I could implement a cleaner transformation of the TeamBattleLog to its text and html representation.

But anyways, I think the end result is good!
