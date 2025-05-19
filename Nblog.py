# blog.py
import urllib.request
import urllib.parse
import json
import re

# 🔑 네이버 API 정보 입력
client_id = "client_id"
client_secret = "secret"

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)

def search_blog(query):
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}&display=5"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read()
            data = json.loads(response_body.decode('utf-8'))

            result = []
            for item in data['items']:
                result.append({
                    "title": clean_html(item.get("title", "")),
                    "link": item.get("link", ""),
                    "description": clean_html(item.get("description", "")),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                })
            return result
        else:
            print("API Error Code:", rescode)
            return []

    except Exception as e:
        print("API 호출 중 예외 발생:", e)
        return []