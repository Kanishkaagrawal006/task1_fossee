from general_tree import *

# ---------- LOAD TREE ----------
root = build_tree_from_yaml("test.yaml")

print("Initial tree:")
print_tree(root)

# ---------- SAVE TREE ----------
write_tree_to_yaml(root, "output.yaml")
