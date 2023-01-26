import openai
openai.api_key = "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"
def tell_me(arg):
	response = openai.Completion.create(
	model="text-davinci-003",
	prompt=arg,
	temperature=0.9,
	max_tokens=150,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0.6,
	stop=[" Human:", " AI:"]
	)
	text = response['choices'][0]['text']
	return text