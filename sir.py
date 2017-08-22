num1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
num3 = {1 :'One Hundred', 2:'Two Hundred', 3:'Three Hundred', 4:'Four Hundred', 5:'Five Hundred' , 6:'Six Hundred', 7:'Seven Hundred', 8:'Eight Hundred', 9:'Nine Hundred'}
global r
r = []
def numberAlpha(n):
    if (n >= 1) and (n <= 19):
        r.append (num1[n])
    elif (n>=20) and (n<=99):
        a=n//10
        b=n%10
        if b==0:
            r.append (num2[a])
        else:
            r.append (num2[a] + " " +num1[b])
    elif (n>=100) and (n<=999):
        c=n//100
        r.append(" " + num3[c])
        d=n%100
        numberAlpha(d)
    else:
        print('Not in range')

    return ("".join(r)) 

print(numberAlpha(900))

