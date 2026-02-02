import yaml
from .node import Node


# ---------- BUILD TREE FROM YAML ----------
def build_tree_from_yaml(yaml_file):
    """Build a general tree from YAML."""
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError("YAML file is empty or invalid")

    def build(node_data):
        if node_data is None:
            return None

        node = Node(node_data["value"])

        for child_data in node_data.get("children", []):
            child = build(child_data)
            if child:
                node.children.append(child)

        return node

    return build(data)


# ---------- TREE TO DICTIONARY ----------
def tree_to_dict(root):
    """Convert general tree to dictionary."""
    if root is None:
        return None

    result = {"value": root.value}

    if root.children:
        result["children"] = [tree_to_dict(child) for child in root.children]

    return result


# ---------- WRITE TREE TO YAML ----------
def write_tree_to_yaml(root, yaml_file):
    """Write general tree to YAML."""
    tree_dict = tree_to_dict(root)

    with open(yaml_file, "w") as f:
        yaml.dump(tree_dict, f, sort_keys=False)
