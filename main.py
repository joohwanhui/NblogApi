# main.py
from Nblog import search_blog

def main():
    print("🍜 네이버 블로그 맛집 검색기")
    keyword = input("검색할 맛집 키워드를 입력하세요: ").strip()

    if not keyword:
        print("❗ 키워드를 입력해주세요.")
        return

    results = search_blog(keyword)

    if results:
        print(f"\n📌 '{keyword}' 검색 결과:")
        for i, item in enumerate(results, start=1):
            print(f"\n[{i}] 제목: {item['title']}")
            print(f"    링크: {item['link']}")
            print(f"    설명: {item['description']}")
            print(f"    블로거: {item['bloggername']} | 작성일: {item['postdate']}")
    else:
        print("검색 결과가 없습니다.")

if __name__ == "__main__":
    main()