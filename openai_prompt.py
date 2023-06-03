import openai

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="siapa presiden indonesia",
    temperature=0.7,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
print(response)
print(response.choices[0].text)