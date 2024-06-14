import datetime
import pytz

seoul_tz = pytz.timezone('Asia/Seoul')
now = datetime.datetime.now(seoul_tz)
print("현재 한국 시간:", now.strftime('%Y-%m-%d %H:%M:%S'))


timezones = {
    '미국 뉴욕': 'America/New_York',
    '영국 런던': 'Europe/London',
    '일본 도쿄': 'Asia/Tokyo',
    '호주 시드니': 'Australia/Sydney',
    '독일 베를린': 'Europe/Berlin'
}

for city, tz in timezones.items():
    city_tz = pytz.timezone(tz)
    city_time = now.astimezone(city_tz)
    print(f"현재 {city} 시간: {city_time.strftime('%Y-%m-%d %H:%M:%S')}")
