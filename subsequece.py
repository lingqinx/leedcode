from numpy import zeros

def longest_common_subsequence(s,t):
    lens=zeros((len(s)+1,len(t)+1))
    #print(lens)
    for i in range(len(s)):
        for j in range(len(t)):
            
            if suba[i]==subb[j]:
                lens[i+1][j+1]=lens[i][j]+1
            else:
                lens[i+1][j+1]=max(lens[i+1][j],lens[i][j+1])
    result=''
    i+=1
    j+=1
    while i*j != 0:
            
        if lens[i-1][j]==lens[i][j]:
            i-=1
        elif lens[i][j]==lens[i][j-1]:
            j-=1
        else:
            result+=suba[i-1]
            i-=1
            j-=1            
    return lens[len(s)+1,len(t)+1],result[::-1]

def l_increase_subseq(seq):
    m = [0]*length
    for x in range(length-2,-1,-1):
        for y in range(length-1,x,-1):
            if int(seq[x])<int(seq[y]) and m[x]<=m[y]:
                m[x]+=1
        max_value = max(m)
        result = []
        for i in range(length):
            if m[i] == max_value:
                result.append(int(seq[i]))
                max_value -=1
    return result
def l_decrease_subseq(seq):
    m = [0]*length
    for x in range(length-2,-1,-1):
        for y in range(length-1,x,-1):
            if int(seq[x])>int(seq[y]) and m[x]<=m[y]:
                m[x]+=1
        max_value = max(m)
        result = []
        for i in range(length):
            if m[i] == max_value:
                result.append(int(seq[i]))
                max_value -=1
    return result

def substring_position(A,B):
    position = []
    for i in range(len(A)-len(B)):
        if A[i:i+len(B)] == B:
            position.append(str(i+1))
    return position
