import random
import requests
from django.shortcuts import render

# Create your views here.


def tryLotto(arr, bonus):
    counts = [0] * 6
    for _ in range(1000):
        isBonus = 0
        cnt = 0
        for _ in range(6):
            rand = random.randrange(1, 46)
            if rand == bonus:
                isBonus = 1
            if rand in arr:
                cnt += 1
        if cnt == 6:
            counts[1] += 1
        elif cnt == 5:
            if isBonus:
                counts[2] += 1
            else:
                counts[3] += 1
        elif cnt == 4:
            counts[4] += 1
        elif cnt == 3:
            counts[5] += 1
        else:
            counts[0] += 1
    return counts


def recommendNumber():
    recommendList = []
    for _ in range(6):
        rand = random.randrange(1, 46)
        recommendList.append(rand)
    return recommendList


def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'dinner.html', context)


def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1004'
    response = requests.get(url)
    result = response.json()
    lottoNumbers = []

    lottoNumbers.append(result['drwtNo1'])
    lottoNumbers.append(result['drwtNo2'])
    lottoNumbers.append(result['drwtNo3'])
    lottoNumbers.append(result['drwtNo4'])
    lottoNumbers.append(result['drwtNo5'])
    lottoNumbers.append(result['drwtNo6'])
    bnusNo = result['bnusNo']

    counts = tryLotto(lottoNumbers, bnusNo)
    recommendList = recommendNumber()

    context = {
        'lottoNumbers': lottoNumbers,
        'bnusNo': bnusNo,
        'counts': counts,
        'recommendList': recommendList,
    }
    return render(request, 'lotto.html', context)
