def humanName(s):
    ans = 0
    i = 0
    while i < len(s):        
        if(s[i].isupper()):
            cnt = 1
            for j in range (i + 2, len(s)):                
                if(s[j].isupper() and s[j-1] == ' '):
                    cnt += 1
                if((s[j].islower() and s[j-1] == ' ') or (j == len(s) - 1)):
                    if cnt >= 3:
                        ans += 1
                    i = j
                    break
        i += 1
    return ans

#--------------------------------------
def isDigit(c):
    return '0' <= c and c <= '9'
def dob(s):
    ans = 0
    i = 0
    while i < len(s):
        if(isDigit(s[i])):
            cnt = 0
            for j in range(i + 1, len(s)):
                if(s[j] == '/' or s[j] == '-' or s[j] == '.'):
                    cnt += 1
                else:
                    if(not isDigit(s[j]) or j == len(s) - 1):
                        if cnt == 2:
                            ans += 1
                        i = j
                        break
        i += 1
    return ans

#---------------------------------------------
def account_phone(s):
    s = s + '*'
    ans = 0
    i = 0
    while i < len(s):
        if(isDigit(s[i])):
           cnt = 1
           for j in range(i + 1, len(s)):
              if(isDigit(s[j]) or s[j] == ' '):
                  cnt += 1
              else:
                  if cnt == 9 or cnt == 10 or cnt == 12:
                      ans += 1
                  i = j
                  break

        i += 1
    return ans

# count email --------------------
def email(s):
    ans = 0
    i = 0
    while i < len(s):
        if s[i] == '@':
            has_dot = False
            for j in range(i + 1, len(s)):
                if(s[j] == '.' and j != len(s) - 1):
                    has_dot = True
                if(s[j] == ' ' or j == len(s) - 1):
                    if has_dot:
                        ans += 1
                    i = j
                    break
        i += 1
    return ans

f = open('type1.txt', 'r')

cnt_name = 0
cnt_dob = 0
cnt_acc = 0
cnt_email = 0
cnt_line = 0

for line in f:    
    cnt_name += humanName(line)
##    if(humanName(line) < 1):
##        print line
    cnt_dob += dob(line)
    cnt_acc += account_phone(line)
    cnt_email += email(line)
    cnt_line += 1
    

print "cnt_name = ",
print cnt_name
print "cnt_dob = ",
print cnt_dob
print "cnt_acc = ",
print cnt_acc
print "cnt_email = ",
print cnt_email
print "cnt_line = ",
print cnt_line
