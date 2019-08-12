def reverse(string, way='e'):
    '''
    This function will reverse strings the Python easy way
    and the hard way most launguages use.
    '''
    if way == 'e':
        def easy(string):
            '''
            The easy way: Use the reverse index O(n)
            '''
            print("The easy way:")
            return string[::-1]
        return easy(string)
    if way == 'h':
        def hard(string):
            '''
            The hard way: convert string to list, reverse list, join list as string 
            also O(n)
            '''
            print("The hard way:")
            l = list(string)
            l.reverse()
            return str(''.join(l))
        return hard(string)
    else:
        def hardest(string):
            '''
            One more way to do it without converting to list.
            Requires loop.
            still O(n)
            '''
            print("The hardest way:")
            s = ''
            i = len(string)-1
            while i > -1:
                s = s + string[i]
                i-=1
            return s
        return hardest(string)




if __name__ == "__main__":

    s = "Let's try this string."
    print(reverse(s,'e'))
    print(reverse(s,'h'))
    print(reverse(s,'x'))
