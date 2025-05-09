def mirrorImage(root):

    if root is None:
        return

    root.left, root.right = root.right, root.left
    
    mirrorImage(root.left)
    mirrorImage(root.right)

