import datetime

now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')

with open("index.html", 'w') as f:
    f.write(f'Last updated at {current_time}')

    #현재 시각을 마지막 업데이트 시각으로 보여주는 파일.