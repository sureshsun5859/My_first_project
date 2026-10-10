
def remove_invalid_parentheses(expression):
    """
    Args:
     expression(str)
    Returns:
     list_str
    """
    # Write your code here.
    valid_expressions = set()

    def helper(id, expression, current_expression, no_of_left_parentheses, no_of_right_parentheses, left_rem, right_rem,
               removal_count):
        if id == len(expression):
            # Checking validity of 'current_expression'.
            if left_rem == 0 and right_rem == 0:
                valid_expressions.add(''.join(current_expression))
        else:
            # Not taking current parenthesis.
            if expression[id] == '(' and left_rem > 0:
                helper(id + 1, expression, current_expression,
                       no_of_left_parentheses, no_of_right_parentheses, left_rem - 1, right_rem,
                       removal_count + 1)
            elif expression[id] == ')' and right_rem > 0:
                helper(id + 1, expression, current_expression,
                       no_of_left_parentheses, no_of_right_parentheses, left_rem, right_rem - 1,
                       removal_count + 1)
            # Taking current parenthesis in the 'current_expression'.
            current_expression.append(expression[id])
            if expression[id] not in {'(', ')'}:
                helper(id + 1, expression, current_expression,
                       no_of_left_parentheses, no_of_right_parentheses, left_rem, right_rem, removal_count)
            elif expression[id] == '(':
                helper(id + 1, expression, current_expression,
                       no_of_left_parentheses + 1, no_of_right_parentheses, left_rem, right_rem, removal_count)
            # Checking the validity of 'current_expression' on the go.
            elif no_of_left_parentheses > no_of_right_parentheses:
                helper(id + 1, expression, current_expression,
                       no_of_left_parentheses, no_of_right_parentheses + 1, left_rem, right_rem, removal_count)
            current_expression.pop()

    # Find out the minimum number of left and right parentheses to be removed.
    extra_left = 0
    extra_right = 0
    for char in expression:
        if char == '(':
            extra_left += 1
        elif char == ')':
            if extra_left == 0:
                extra_right += 1
            else:
                extra_left -= 1

    current_expression = []
    # Backtrack to find all possible solutions.
    helper(0, expression, current_expression, 0, 0, extra_left, extra_right, 0)
    return list(valid_expressions)

expression = "()())()"
print(remove_invalid_parentheses(expression))