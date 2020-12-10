"""
REVERSE LINKED LIST

Write a function that takes in the 'head' of a singly linked list, reverses the
list in place (i.e. - doesn't create a brand new list), and returns its new
'head'.

Each 'LinkedList' node has an integer, 'value', as well as a 'next' node
pointing to the next node in the list or to 'None'/'null' if it's the tail of
the list.

You can assume that the input Linked List will always have at least one node; in
other words, the head will never be 'None'/'null'.

Sample Input:
    - head = 0 -> 1 -> 2 -> 3 -> 4 -> 5     # the 'head' node with value 0
    
Sample Output:
    - 5 -> 4 -> 3 -> 2 -> 1 -> 0     # the new 'head' node with value 5
"""

def reverseLinkedList(head):
    # Define the first two pointers that will be used to reverse the linked list
    # at each node.
    p1, p2 = None, head
    
    # Iterate through the linked list so long as the 'p2' pointer does not
    # reach the end of the list.
    while p2 is not None:
        
        # Create a third pointer, p3, that will keep reference to the value of
        # p2.next before p2.next is overwritten to reverse the direction of the
        # linked list AT THIS NODE.
        p3 = p2.next
        
        # Point the 'p2.next' pointer to p2's previous node (i.e. - p1).
        p2.next = p1
        
        # Move the 'p1' pointer forward to the next node to continue iterating
        # through the linked list.
        p1 = p2
        
        # Move the 'p2' pointer forward to the next node to continue iterating
        # through the linked list.
        p2 = p3
        
    # Return the value of the new 'head' node.
    return p1