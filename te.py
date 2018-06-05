ko = {'오상원' : 51, '박찬우' : 92, '김문수' : 83}
en = {'오상원' : 63, '박찬우' : 99, '김문수' : 87}
ma = {'오상원' : 39, '박찬우' : 94, '김문수' : 86}
sc = {'오상원' : 42, '박찬우' : 91, '김문수' : 89}
print("            *기능*             ")
print("------------------------------")
print("1번을 입력하면 성적을 조회힙니다.\n2번을 입력하면 이름과 성적을 추가합니다.")
print("3번을 입력하면 이름과 성적을 제거합니다.\n4번을 입력하면 종료합니다.")
print("0번을 입력하면 전체 이름과 성적을 조회합니다.")
print("------------------------------")
while True:
    try:
        fuc = str(input("사용하실 기능을 입력하세요:"))
        if (fuc != '1' and fuc != '2' and fuc != '3' and fuc != '4' and fuc != '0'):
            raise ValueError
    except ValueError:
        print("해당 번호 또는 숫자는 없는 기능입니다.")
    if (fuc == '4'):
        break
    elif (fuc == '1'):
        name = input("성적을 조회할 학우의 이름을 입력하세요:")
        try:
            if (name not in ko.keys() or name not in en.keys() or name not in ma.keys() or name not in sc.keys()):
                raise ValueError
            print("{}의 국어 점수는 {} 입니다.".format(name, ko[name]))
            print("{}의 영어 점수는 {} 입니다.".format(name, en[name]))
            print("{}의 수학 점수는 {} 입니다".format(name, ma[name]))
            print("{}의 과학 점수는 {} 입니다".format(name, sc[name]))
        except ValueError:
            print("해당 학우는 없는 것 같습니다.")
    elif (fuc == '2'):
        plus = input("추가할 학우의 이름을 입력하세요:")
        try:
            if (plus in ko.keys() or plus in en.keys() or plus in ma.keys() or plus in sc.keys()):
                raise ValueError
            plus_ko = int(input("{}의 국어 점수를 입력하세요:".format(plus)))
            ko[plus] = plus_ko
            plus_en = int(input("{}의 영어 점수를 입력하세요:".format(plus)))
            en[plus] = plus_en
            plus_ma = int(input("{}의 수학 점수를 입력하세요:".format(plus)))
            ma[plus] = plus_ma
            plus_sc = int(input("{}의 과학 점수를 입력하세요:".format(plus)))
            sc[plus] = plus_sc
            print("{}학우가 정상적으로 추가되었습니다.".format(plus))
        except ValueError:
            print("해당 학우는 이미 있습니다.")
    elif (fuc == '3'):
        delete = input("삭제할 학우의 이름을 입력하세요:")
        try:
            if (delete not in ko.keys() or delete not in en.keys() or delete not in ma.keys() or delete not in sc.keys()):
                raise ValueError
            del(ko[delete])
            del(en[delete])
            del(ma[delete])
            del(sc[delete])
            print("{}학우의 성적이 정상적으로 제거되었습니다.".format(delete))
        except ValueError:
            print("해당 학우는 없는 것 같습니다.")
    elif (fuc == '0'):
        print("국어-{}\n영어-{}\n수학-{}\n과학-{}".format(ko, en, ma, sc))
