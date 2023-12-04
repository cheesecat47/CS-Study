"""
스터디 일시: Mon Dec  4 14:47:32 2023
참여 인원: ['김철수', '홍길동', '이영희']
오늘의 발표자: 김철수
질문 -> 답변
	김철수 -> 이영희	홍길동 -> 김철수	이영희 -> 홍길동
"""

import json
import random
from datetime import datetime

with open("member.json", "r", encoding="utf-8") as fin:
    print(f"스터디 일시: {datetime.strftime(datetime.now(), '%c')}")

    members = json.load(fin)['members']
    print(f"참여 인원: {members}")

    # 오늘의 발표자 한 명 뽑기
    print(f"오늘의 발표자: {random.choice(members)}")

    # 질문 -> 답변
    members_shuffled = members.copy()
    while True:
        # 멤버 목록 섞고
        random.shuffle(members_shuffled)

        # 질문 == 답변 있는지 확인
        diff = [True for (m1, m2) in zip(members, members_shuffled) if m1 == m2]

        # 질문 == 답변 없다면 끝, 있다면 다시 섞기
        if len(diff) == 0:
            break

    print("질문 -> 답변")
    for idx, (m1, m2) in enumerate(zip(members, members_shuffled)):
        print(f"\t{m1} -> {m2}", end="\n" if idx % 3 == 2 else "")
