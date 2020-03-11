def connect(root):
    if root:
        if root.nextRight:
            if root.right and root.nextRight.left:
                root.right.nextRight = root.nextRight.left
            elif root.left and root.nextRight.left:
                root.left.nextRight = root.nextRight.left
            elif root.right and root.nextRight.right:
                root.right.nextRight = root.nextRight.right
            elif root.left and root.nextRight.right:
                root.left.nextRight = root.nextRight.right
        if root.left and root.right:
            root.left.nextRight = root.right
        if root.left:
            connect(root.left)
        if root.right:
            connect(root.right)