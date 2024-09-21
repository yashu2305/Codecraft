"""" Q.1] Reverse a Stack You are given a stack of integers. Your task is to
reverse the order of the elements in the stack using only stack
operations (push and pop) and without using any additional data
structures"""
def reverse_stack(stack):
    if not stack:
        return
    
    top = stack.pop()
    
    reverse_stack(stack)
    
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    
    # Step 1: Pop all elements
    top = stack.pop()
    
    # Step 2: Insert the item at the bottom
    insert_at_bottom(stack, item)
    
    # Step 3: Push the popped element back
    stack.append(top)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack) 
