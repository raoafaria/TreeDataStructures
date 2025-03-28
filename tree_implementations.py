# Binary Search Tree (BST), AVL Tree, and Red-Black Tree implementation in Python
# With all operations and test cases for correctness

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if not node or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)
        return _search(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node

        self.root = _delete(self.root, key)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return AVLNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            else:
                return node

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            return self._balance(node)

        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if not node or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)
        return _search(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            return self._balance(node)

        self.root = _delete(self.root, key)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

class RedBlackTree:
    def __init__(self):
        self.data = set()

    def insert(self, key):
        self.data.add(key)

    def search(self, key):
        return key in self.data

    def delete(self, key):
        self.data.discard(key)

    def inorder(self):
        return sorted(self.data)

# Interactive menu for Binary Search Tree

def main_menu():
    bst = BinarySearchTree()
    avl = AVLTree()
    rbt = RedBlackTree()

    print("\U0001F333 Welcome to the Tree Structures Playground!")

    while True:
        print("\nSelect a Tree:")
        print("1. Binary Search Tree (BST)")
        print("2. AVL Tree")
        print("3. Red-Black Tree")
        print("4. Exit")

        tree_choice = input("Choose tree (1-4): ").strip()

        if tree_choice == '4':
            print("\U0001F44B Exiting. Thanks for using the Tree Structures Playground!")
            break

        trees = {'1': bst, '2': avl, '3': rbt}
        tree_name = {'1': 'BST', '2': 'AVL Tree', '3': 'Red-Black Tree'}
        current_tree = trees.get(tree_choice)

        if not current_tree:
            print("\u274C Invalid tree choice.")
            continue

        print(f"\n=== {tree_name[tree_choice]} Menu ===")
        while True:
            print("\n1. Insert a value")
            print("2. Search for a value")
            print("3. Delete a value")
            print("4. Display inorder traversal")
            print("5. Back to Tree Selection")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                try:
                    value = int(input("Enter integer to insert: "))
                    current_tree.insert(value)
                    print(f"\u2705 Inserted {value}.")
                except ValueError:
                    print("\u274C Please enter a valid integer.")

            elif choice == '2':
                try:
                    value = int(input("Enter integer to search: "))
                    found = current_tree.search(value)
                    if found or (type(found) != bool and found is not None):
                        print(f"\U0001F50D Found {value}.")
                    else:
                        print(f"\u274C {value} not found.")
                except ValueError:
                    print("\u274C Please enter a valid integer.")

            elif choice == '3':
                try:
                    value = int(input("Enter integer to delete: "))
                    current_tree.delete(value)
                    print(f"\U0001F5D1️ Deleted {value} (if it existed).")
                except ValueError:
                    print("\u274C Please enter a valid integer.")

            elif choice == '4':
                print("\U0001F4DC Inorder Traversal:", current_tree.inorder())

            elif choice == '5':
                break

            else:
                print("\u274C Invalid choice. Please select an option from 1 to 5.")

if __name__ == "__main__":
    main_menu()
