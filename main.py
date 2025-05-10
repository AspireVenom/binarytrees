from binarytree import tree, bst, heap, build

def generate_trees():
    while True:
        user_input = input("\nEnter tree height (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting.")
            break
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        height = int(user_input)

        print("\nRandom Binary Tree:")
        print(tree(height=height))

        print("\nRandom Binary Search Tree (BST):")
        print(bst(height=height))

        print("\nRandom Max-Heap:")
        print(heap(height=height))

# Run the function
generate_trees()
