class Solution(object):
    def strStr(self, haystack, needle='-1'):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        str(needle)

        def check_space(s):
            for x in iter(str(s)):
                if x != ' ':
                    return True
            return False
        
        def get_index(h,n, store=[]):
            for index, value in enumerate(iter(h)):
                if value == n[0]:
                    store.append(index)
            if len(store) == 1:
                return store[0]
            for index, value in enumerate(store):
                if n in h[value:value+len(n)]:
                    return store.pop(index)
            return store[0]

        
        if needle == '':
            return 0
        elif check_space(needle) == False:
            return 0                
        elif needle in haystack:
            return get_index(haystack,needle)
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr('haystack', 'needle'))
    print(s.strStr('haystack', 'st'))
    print(s.strStr('haysackst', 'st'))
    print(s.strStr('haystackst', 'st'))
    print(s.strStr('    1   ', '1'))
    print(s.strStr('       ', '  '))
    print(s.strStr('    1   ', ''))
    print(s.strStr('    1   ', ' 1 '))
    print(s.strStr("mississippi", "sipp"))

    # f = 'haysackst'
    # k = 'st'
    # print(len(f))
    # print(len(k))
    # for index, value in enumerate(iter(f)):
    #     if value == 's':
    #         print('get st:', f[index:index+len(k)])