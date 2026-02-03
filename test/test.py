from general_tree import *
def main():
    # ------------------ CREATE TREE ------------------
    print("=== Creating Initial Tree ===")
    root = Node(10)
    print_tree(root)

    # ------------------ ADD NODES ------------------
    print("\n=== Adding Nodes ===")
    add_node(root, 10, 5)
    add_node(root, 10, 15)
    add_node(root, 5, 3)
    add_node(root, 5, 7)
    add_node(root, 15, 12)
    add_node(root, 15, 18)
    print_tree(root)

    # ------------------ EDIT NODE ------------------
    print("\n=== Editing Node ===")
    edit_node(root, 7, 8)      # Change 7 → 8
    print_tree(root)

    # ------------------ DELETE NODE ------------------
    print("\n=== Deleting Node ===")
    root = delete_node(root, 12)  # Delete node 12
    print_tree(root)

    # ------------------ PRINT RANGE ------------------
    print("\n=== Printing Nodes in Range 5-15 ===")
    print_range(root, 5, 15)

if __name__ == "__main__":
    main()

# ---------- LOAD TREE ----------
root = build_tree_from_yaml("test.yaml")

print("Initial tree:")
print_tree(root)

# ---------- SAVE TREE ----------
write_tree_to_yaml(root, "output.yaml")
