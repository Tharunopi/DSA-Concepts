"""
dls_Stack() - Adds the link to the head of the list.
dls_Queue() - Adds the link to the tail of the list.
dls_AddAfter() - Adds the link to a list after another specified link.
dls_AddBefore() - Adds the link to a list before another specified link.
dls_Pop() - Removes and returns the link at the head of the list.
dls_PopTail() - Removes and returns the link at the tail of the list.
dls_Remove() - Remove a specified link from the list.
dls_Peek() - Returns the link at the head of the list without removing it.
dls_PeekTail() - Returns the link at the tail of the list without removing it.
dls_PeekNext() - Returns the link next to a specified link without removing it.
dls_PeekPrev() - Returns the link previous to a specified link without removing it.
dls_Swap() - Swaps the position of two links in a list.
dls_IsEmpty() - Checks if a given list is empty.
dls_IsInList() - Checks if a specified link is in the list.
dls_NumLinks() - Checks the number of links currently in the list.
"""

from linked_lists import Node

def dls_stack(old_node, value):
    """Adds the link to the head of the list."""
    new_node = Node(value)
    if old_node:
        new_node.next = old_node
        old_node.prev = new_node
    return new_node

def dls_queue(old_node, value):
    """Adds the link to the tail of the list."""
    new_node = Node(value)
    if old_node:
        cur = old_node
        while cur:
            if cur.next is None:
                cur.next = new_node
                new_node.prev = cur
                return old_node
            cur = cur.next 
    return new_node

def add_after(old_node, find_value, insert_value):
    """Adds the link to a list after another specified link."""
    new_node = Node(insert_value)
    if old_node:
        cur = old_node
        while cur:
            if cur.value == find_value:
                if cur.next:
                    next_node = cur.next 
                    new_node.next = next_node
                    next_node.prev = new_node
                    cur.next = new_node
                    new_node.prev = cur
                    return old_node
                else:
                    cur.next = new_node
                    new_node.prev = cur
                    return old_node
    return new_node

def add_before(old_node, find_value, insert_value):
    """Adds the link to a list before another specified link."""
    new_node = Node(insert_value)

    if old_node.value == find_value:
        new_node.next = old_node
        old_node.prev = new_node
        return new_node
    
    if old_node:
        cur = old_node
        while cur:
            if cur.value == find_value:
                prev_node = cur.prev
                prev_node.next = new_node
                new_node.prev =prev_node
                new_node.next = cur
                cur.prev = new_node
                return old_node
            cur = cur.next
        
    return new_node

def dls_pop(old_node):
    """dls_Pop() - Removes and returns the link at the head of the list."""
    return old_node.next

def dls_poptail(old_node):
    """Removes and returns the link at the tail of the list."""
    if cur.next is None:
        return None
    
    cur = old_node
    while cur.next:
        cur = cur.next
    
    cur.next = None
    return old_node

def dls_remove(old_node, value):
    """Remove a specified link from the list."""
    if old_node.value == value:
        return old_node.next
    
    if old_node:
        cur = old_node
        while cur:
            if cur.value == value:
                prev_node = cur.prev 
                next_node = cur.next
                prev_node.next = next_node
                next_node.prev = prev_node
                return old_node
            cur = cur.next
    return "Not Found"

def peek(old_node):
    """Returns the link at the head of the list without removing it."""
    if old_node:
        cur = old_node
        while cur.prev:
            cur = cur.prev
        return cur
    
def peek_tail(old_node):
    """Returns the link at the tail of the list without removing it."""
    if old_node:
        cur = old_node
        while cur.next:
            cur = cur.next
        return cur
    
def peek_next(old_node, value):
    """Returns the link next to a specified link without removing it."""
    if old_node.value == value:
        return old_node.next
    
    if old_node:
        cur = old_node
        while cur:
            if cur.value == value:
                if cur.next:
                    return cur.next
                else:
                    return None
            cur = cur.next

def peek_prev(old_node, value):
    """Returns the link previous to a specified link without removing it."""
    if old_node.value == value:
        return old_node.prev
    
    if old_node:
        cur = old_node
        while cur:
            if cur.value == value:
                return cur.prev
            cur = cur.next
    return None

def swap(old_node, position_1, postion_2):
    """Swaps the position of two links in a list."""

    if not old_node or position_1 == postion_2:
        return old_node

    if position_1 and postion_2 and old_node:
        cur = old_node
        i = 1
        while cur:
            if position_1 == i:
                node_1 = cur
            if postion_2 == i:
                node_2 = cur
            cur = cur.next
            i += 1
        if node_1 and node_2:
            node_1.value, node_2.value = node_2.value, node_1.value
        return old_node
    
def dlf_isempty(old_node):
    """Checks if a given list is empty."""
    if old_node:
        return True
    return False


def isinlist(old_node, value):
    """Checks if a specified link is in the list."""
    if old_node:
        cur = old_node
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
    return False

def numlinks(old_node):
    """Checks the number of links currently in the list."""
    if not old_node:
        return 0
    i = 0
    cur = old_node
    while cur:
        i += 1
        cur = cur.next
    return i