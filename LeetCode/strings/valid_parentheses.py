def valid(s):
    '''
        takes in string with '({[)}])'
        if parentheses open and close in proper order
        return True
        valid: ({[]})
        invalid: ([)]
        empty strings are valid
    '''
    # check if string is empty
    if s == '':
        return True
    # make sure even number of inputs
    if len(s)%2 != 0:
        return False
    # create stack to add valid open parenthesis
    # last on, first off
    stack = []
    # list valid starting parenthesis
    open = set('({[')
    # list valid matching parenthesis
    match = set([('(',')'), ('{', '}'), ('[', ']')])
    # iterate through string
    for v in s:
        # if the value is in open
        if v in open:
            # it is valid to add to the stack
            stack.append(v)
        else:
            # if there is nothing on the stack
            # and there is a closed parenthesis
            # it is invalid
            if stack == []:
                return False
            # get the top item from the stack
            last = stack.pop()
            # if the open parenthesis and the closed don't match
            if (last, v) not in match:
                # invalid
                return False
    # if the stack is empty, the parenthesis were all valid
    return stack == []
    
if __name__ == "__main__":
    print(valid("(]"))
    print(valid(''))
    print(valid("([)]"))
    print(valid("()[]{}"))

