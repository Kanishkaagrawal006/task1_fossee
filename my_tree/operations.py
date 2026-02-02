from .node import Node
from collections import deque

# ---------- PRINT TREE ----------
def print_tree(root, level=0, label="Root:"):
    if root is None:
        return

    indent = " " * (4 * level)
    print(f"{indent}{label}{root.value}")

    for i, child in enumerate(root.children):
        print_tree(child, level + 1, f"C{i+1}---")


# ---------- PRINT RANGE ----------
def print_range(root, low, high):
    if root is None:
        return

    if low <= root.value <= high:
        print(root.value)

    for child in root.children:
        print_range(child, low, high)


# ---------- ADD NODE ----------
def add_node(root, parent_value, value):
    """
    Add node under parent_value
    """
    if root is None:
        return False

    q = deque([root])
    while q:
        current = q.popleft()
        if current.value == parent_value:
            current.children.append(Node(value))
            return True
        for child in current.children:
            q.append(child)

    return False


# ---------- EDIT NODE ----------
def edit_node(root, old_value, new_value):
    if root is None:
        return False

    q = deque([root])
    while q:
        current = q.popleft()
        if current.value == old_value:
            current.value = new_value
            return True
        for child in current.children:
            q.append(child)

    return False


# ---------- DELETE NODE ----------
def delete_node(root, value):
    if root is None:
        return None

    # If root is to be deleted
    if root.value == value:
        if not root.children:
            return None
        new_root = root.children[0]
        new_root.children.extend(root.children[1:])
        return new_root

    q = deque([(root, None)])
    while q:
        current, parent = q.popleft()
        if current.value == value and parent:
            parent.children.remove(current)
            parent.children.extend(current.children)
            return root
        for child in current.children:
            q.append((child, current))

    return root
