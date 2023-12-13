#GET https://newsapi.org/v2/everything?q=bitcoin&apiKey=4fccf9a9200744178deeb56b77c2cc2f
from newsapi import NewsApiClient
from openai import OpenAI
client = OpenAI(api_key="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")

newsapi = NewsApiClient(api_key='4fccf9a9200744178deeb56b77c2cc2f')


def getContent(query):
    

    try:
      print("Getting Headlines for " + query)
      newsapi = NewsApiClient(api_key='4fccf9a9200744178deeb56b77c2cc2f')
      top_headlines = newsapi.get_top_headlines(query)
      imgUrl2 = top_headlines['articles'][0]['urlToImage']
      titlezz = top_headlines['articles'][0]['title']
      titlez = str(titlezz)
      descriptions = [article['description'] for article in top_headlines['articles']][:8]
      descriptions[0]
      for i, description in enumerate(descriptions, start=1):
          #list of all articles
          global NewsCont1
          NewsCont1 = ""
          NewsCont1 += (f"Article {i}: {description}")

      response2 = client.chat.completions.create(
        model="gpt-4",
        messages=[
          {"role": "system", "content": "You have to only generate and reply a news blog of 2 page content body. The title, related articles, some content is provided by the user from trusted sources. Skip the title part, start with introduction"},
          {"role": "user", "content": "Here it is "+str(NewsCont1)}
        ]
      )
      bablu = response2.choices[0].message.content
      return titlez,imgUrl2,bablu
        
    except Exception as e:
      print(f"An exception occurred: {str(e)}")
      try:
        newsapi = NewsApiClient(api_key='4fccf9a9200744178deeb56b77c2cc2f')
        print("No Headlines found, using everything now")
        top_headlines = newsapi.get_everything(query)
        imgUrl2 = top_headlines['articles'][0]['urlToImage']
        titlezz = top_headlines['articles'][0]['title']
        titlez = str(titlezz)
        descriptions = [article['description'] for article in top_headlines['articles']][:3]
        descriptions[0]
        for i, description in enumerate(descriptions, start=1):
            #list of all articles
            global NewsCont
            NewsCont = ""
            NewsCont += (f"Article {i}: {description}")
        response2 = client.chat.completions.create(
        model="gpt-4",
        messages=[
          {"role": "system", "content": "The title, related articles, some content is provided by the user from trusted sources. You have to only generate and reply a news blog of 1 page content body only.Your reply will be pasted directly inside the body of article. Skip the title part and start with introduction directly"},
          {"role": "user", "content": "Here it is "+str(NewsCont)}
        ]
        )
        bablu = response2.choices[0].message.content
        return titlez,imgUrl2,bablu

      except Exception as e:
        
        print(f"An exception occurred: {str(e)}")
        a = "No Articles found, try searching with other keywords"
        b = "No Articles found, try searching with other keywords"
        c = "No Articles found, try searching with other keywords"
        return a,b,c


'''ActualCont = getContent(query="Cricket")
print(ActualCont)'''




#print("hello "+str({Articles}))
#print('You can also search for other articles!')


