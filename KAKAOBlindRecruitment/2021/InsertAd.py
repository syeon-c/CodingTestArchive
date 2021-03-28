def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def solution(play_time, adv_time, logs):
    answer = ''
    # 재생시간, 광고시간 초단위로 변환
    play_time_sec = str_to_int(play_time)
    adv_time_sec = str_to_int(adv_time)
    # 초 단위의 총 재생시간 배열 생성
    total_time = [0 for i in range(play_time_sec + 1)]

    for l in logs:
        logs_start, logs_end = l.split('-')
        # 동영상 재생 구간의 시작 시점과 종료 시점 초단위로 변환
        logs_start_sec = str_to_int(logs_start)
        logs_end_sec = str_to_int(logs_end)
        # total_time[x] = x시각에 시작된 재생 구간의 개수 - x시각에 종료된 재생구간의 개수/ x시각에 시청 중인 사람의 수
        total_time[logs_start_sec] += 1
        total_time[logs_end_sec] -= 1
    print(total_time)

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    print(total_time)

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    print(total_time)

    most_view = 0
    max_time = 0

    # 구간별 누적 시청자 수를 바탕으로 가장 시청자 수가 많은 구간 탐색
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1

    answer += int_to_str(max_time)
    return answer


playTime = "00:00:30"
advTime = "00:00:05"
logs = ["00:00:03-00:00:08", "00:00:11-00:00:20", "00:00:05-00:00:10", "00:00:17-00:00:25", "00:00:10-00:00:20"]

print(solution(playTime, advTime, logs))