import g4f

response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=[{
    	"role": "user", 
    	"content": "Hello World :) I need to translate a big text. Do you have constranit for charachter, if which max simvol for you?",
    }],
    timeout=300,
)

print(f"Result:", response) 