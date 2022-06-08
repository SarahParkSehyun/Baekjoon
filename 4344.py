#대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
n=int(input())
for i in range(n):
    lst=list(map(int,input().split()))
    num=lst[0]
    av=sum(lst[1:])/num
    cnt=0
    for j in lst[1:]:
        if j>av:
            cnt+=1
    a=cnt/num*100
    print("{:.3f}".format(a) + "%")
