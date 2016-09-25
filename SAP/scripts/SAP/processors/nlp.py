# Copyright (c) 2014 The MITRE Corporation. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import logging


class Processor(object):

    def __init__(self, rule_files=None):
        """
        Default initializer.

        Sets up logging and rules.

        """
        # Handle logger
        self.logger = logging.getLogger('bulk')
        self._rule_files = rule_files

    def __str__(self):
        """
        Pretty way to print the processor.
        """
        s = 'Processor ' + __name__
        if self._rule_files:
            s += ' running with rules ' + ' '.join(self._rule_files.values())

        return s
    def match(self, data):
        cnt_name = 0
        cnt_dob = 0
        cnt_acc = 0
        cnt_email = 0
        cnt_line = 0

        for line in data:    
            cnt_name += self.humanName(line)
            cnt_dob += self.dob(line)
            cnt_acc += self.account_phone(line)
            cnt_email += self.email(line)
            cnt_line += 1

        sum = cnt_name + cnt_dob + cnt_acc + cnt_email
        if sum > 100 or sum > cnt_line:
            return True
        else:
            return False
        return True

    def humanName(self, s):
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
    def isDigit(self, c):
        return '0' <= c and c <= '9'
    def dob(self, s):
        ans = 0
        i = 0
        while i < len(s):
            if(self.isDigit(s[i])):
                cnt = 0
                for j in range(i + 1, len(s)):
                    if(s[j] == '/' or s[j] == '-' or s[j] == '.'):
                        cnt += 1
                    else:
                        if(not self.isDigit(s[j]) or j == len(s) - 1):
                            if cnt == 2:
                                ans += 1
                            i = j
                            break
            i += 1
        return ans

    def account_phone(self, s):
        s = s + '*'
        ans = 0
        i = 0
        while i < len(s):
            if(self.isDigit(s[i])):
               cnt = 1
               for j in range(i + 1, len(s)):
                  if(self.isDigit(s[j]) or s[j] == ' '):
                      cnt += 1
                  else:
                      if cnt == 9 or cnt == 10 or cnt == 12:
                          ans += 1
                      i = j
                      break

            i += 1
        return ans

    def email(self,s):
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
    