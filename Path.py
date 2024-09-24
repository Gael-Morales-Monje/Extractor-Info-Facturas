import os

def ExtractPaths(path):
    ArrayPath = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            ArrayPath.append(os.path.join(root,filename))

    return ArrayPath
