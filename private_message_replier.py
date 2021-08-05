"""
	Reddit Private Message Replier Bot
	Author: GrumpyCrouton
	Github: https://github.com/GrumpyCrouton/GCRedditBots
	Version: 1.0
	
	Instructions:
	
		1) Create an account on Reddit for the bot.
		2) On that account, go to https://www.reddit.com/prefs/apps/
		3) Click "are you a developer? create an app..."
		4) Name your app, and select "script" as the type, and put any url for "redirect uri", such as "http://localhost".
		
		5) Now that you have the client ID and secret, you can fill out any of the inputs in the SETTINGS section below.
	
"""
import praw


################ SETTINGS ################

reddit = praw.Reddit(
	user_agent="Private Message Replier {ADD UNIQUE STRING HERE}",
	
	#api details
	client_id="",
	client_secret="",
	
	#reddit account details
	username="",
	password="",
)

"""
	responses Dictionary
	Each entry to this dictionary is a key->value pair.
	When the bot reads a private message, it will search the message (and subject) of the private message for any Key listed.
	If a Key is found in the text, it will reply with the related Value.
	If multiple Keys are found, it will reply each related Value in the same order the below Dictionary is, with a line break between responses.
"""
responses = {
	"hello": "Hello there,",
	"message": "You are correct, this is, in fact, a message.",
}

"""
	keyword_case_sensitive Boolean
	This boolean controls whether or not the Key from the above responses Dictionary should be case sensitive or not.
	If this is set to True, the Keys above WILL be case sensitive.
"""
keyword_case_sensitive = False

################ END SETTINGS ################

def main():
	print('Bot Started')
	try:
		for s in reddit.inbox.stream():
		
			text = s.subject + ": " + s.body
			print("Received Message: \n" + text)
			s.mark_read()
			
			if keyword_case_sensitive == False:
				text = text.casefold()
			
			response = []
			for x in responses:
				if x in text:
					response.append(responses[x])
			
			response_string = '\n\n'.join(response)
			
			print("Replying: \n" + response_string)
			s.reply(response_string)
		
		print("End of submission stream")
	except (prawcore.exceptions.Forbidden, prawcore.exceptions.ServerError):
		print('Auth Failed.')
	except:
		traceback.print_exc(file=sys.stdout)
	
if __name__ == "__main__":
	main()
