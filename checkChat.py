from openai import OpenAI
client = OpenAI(api_key="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")
Articles = "Cricket Worldcup 2023 is won by India"

response2 = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You have to only generate and reply a news blog of 1 page content body. The title, related articles, some content is provided by the user from trusted sources"},
    {"role": "user", "content": "Here it is "+str(Articles)}
  ]
)
print(response2.choices[0].message.content)