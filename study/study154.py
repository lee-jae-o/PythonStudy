def recommend_books(genre):
    book_recommendations = {
        '판타지': ['해리 포터 시리즈', '반지의 제왕', '나니아 연대기'],
        'SF': ['듄', '은하수를 여행하는 히치하이커를 위한 안내서', '스노우 크래쉬'],
        '미스터리': ['셜록 홈즈 시리즈', '안드로이드는 전기양의 꿈을 꾸는가?', '오리엔트 특급 살인'],
        '로맨스': ['오만과 편견', '로미오와 줄리엣', '노팅 힐'],
        '역사': ['사피엔스', '군주론', '역사의 역사']
    }
    return book_recommendations.get(genre, "해당 장르의 추천 도서가 없습니다.")

def main():
    print("책 추천 프로그램에 오신 것을 환영합니다.")
    genre = input("원하는 책의 장르를 입력하세요 (예: 판타지, SF, 미스터리, 로맨스, 역사): ")
    
    recommendations = recommend_books(genre)
    if isinstance(recommendations, list):
        print(f"{genre} 장르의 추천 도서 목록:")
        for book in recommendations:
            print(f"- {book}")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()
