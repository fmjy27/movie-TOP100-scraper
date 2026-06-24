import re
import os
import  requests
import csv
from lxml import html

MOVIE_LIST_FILE= "CSV_data/movie_list1.csv"
TMDB_BASE_URL="https://www.themoviedb.org"
TMDB_TOP_URL="https://www.themoviedb.org/movie/top-rated"  #第1页
TMDB_TOP_URL2="https://www.themoviedb.org/discover/movie/items"

# 请求头（必须加，否则容易被拦截）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#发送请求，获取电影详细数据
def get_movie_year(movie_years):
    movie_year=movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(","").replace(")","")


def get_movie_data(movie_dates):
    movie_data=movie_dates[0].strip() if movie_dates else ''
    return re.search(r"\d{4}-\d{2}-\d{2}",movie_data).group()


def get_movie_time(movie_times):
    movie_time=movie_times[0].strip() if movie_times else ''
    h_res=re.search(r"(\d+)h",movie_time)
    m_res=re.search(r"(\d+)m",movie_time)
    h=int(h_res.group(1)) if h_res else 0
    m=int(m_res.group(1)) if m_res else 0
    return h*60+m




def get_movie_info(movie_info_url):
    #发送请求，获取电影详细数据
    movie_response=requests.get(movie_info_url,headers=HEADERS,timeout=60)
    print(f"发送{movie_info_url}情求，获取榜单数据")
    #解析数据，获取电影详情
    movie_doc=html.fromstring(movie_response.text)
    #电影名称
    movie_names=movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/a/text()")
    movie_years=movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_tags = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_times = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_scores = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[2]/div/div/div[1]/div/div[1]/div/div/@data-percent")
    movie_languages = movie_doc.xpath("/html/body/div[1]/main/section/div[3]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_authors = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_slogans = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/h3[1]/text()")
    movie_descriptions = movie_doc.xpath("/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/div/p/text()")
    #组装并返回电影详情
    movie_info={
        "电影名":movie_names[0].strip() if movie_names else '',
        "年份":get_movie_year(movie_years),
        "上映时间":get_movie_data(movie_dates),
        "类型":",".join(movie_tags) if movie_tags else '',
        "时常":get_movie_time(movie_times),
        "评分":movie_scores[0].strip() if movie_scores else '',
        "语言":movie_languages[0].strip() if movie_languages else '',
        "导演":",".join(movie_directors) if movie_directors else '',
        "作者":",".join(movie_authors) if movie_authors else '',
        "slogan类型":movie_slogans[0].strip() if movie_slogans else '',
        "简介":movie_descriptions[0].strip() if movie_descriptions else '',
    }
    return movie_info

#保存至csv
def save_all_movie(all_movies):
    with open(MOVIE_LIST_FILE,"w",encoding="UTF-8",newline="")as csv_file:
        writer=csv.DictWriter(csv_file,fieldnames=["电影名","年份","上映时间","类型","时常","评分","语言","导演","作者","slogan类型","简介"])
        writer.writeheader()
        writer.writerows(all_movies)


# 主函数:定义核心逻辑

def main():
    all_movies = []

    for page_num in range(1,6):#循环获取电影列表（1-5）
        # 发送请求，获取核心数据
        print("发送情求，获取榜单数据")
        if page_num==1:
            response = requests.get(TMDB_TOP_URL, headers=HEADERS, timeout=60) # 请求时间：60秒内
            doc = html.fromstring(response.text)
            movie_list = doc.xpath(
                "/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div[@class='comp:"
                "poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
        else:
            response=requests.post(TMDB_TOP_URL2,
                                    f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-11-08&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400"
                                   ,headers=HEADERS,timeout=60)
            doc = html.fromstring(response.text)
            movie_list = doc.xpath(
                '//div[contains(@class,"poster-card w-full bg-white")]')

        # 解析数据，获取电影列表
        # 遍历列表，获取详情
        for movie in movie_list:
            movie_urls = movie.xpath(".//a[@class='flex w-full']/@href")
            if movie_urls:
                # 电影详情url地址
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详细数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    #存入csv
    print("获取所有电影详情，保存到CSV中")
    save_all_movie(all_movies)

if __name__=="__main__":
    main()
