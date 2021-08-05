# GCRedditBots
Reddit bots made by me

## General Instructions
	
  1) Create an account on Reddit for the bot.
  2) On that account, go to https://www.reddit.com/prefs/apps/
  3) Click "are you a developer? create an app..."
  4) Name your app, and select "script" as the type, and put any url for "redirect uri", such as "http://localhost".

  5) Now that you have the client ID and secret, you can fill out any of the inputs in the SETTINGS section of the bot.

## [Private Message Replier Bot](/private_message_replier.py)
When a private message is received, this bot will loop through a key->value pair of strings, if the Key is found in the private message, the related Value is replied. If multiple Keys are found, each related Value will be replied with a line break between them.

*Please note: This will mark every received private message as read, as that is how it keeps track of which private messages it has already replied to. For a bot account, this is usually no big deal, but if you run this on the account you are actually using, all of your received private messages will pretty much immediately be marked as read.*
