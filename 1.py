import numpy as np

A = np.arange(1, 13).reshape(2, 6)
B, C = np.hsplit(A, 2)
with open("arrays.npy", "wb") as f:
    np.save(f, B)
    np.save(f, C)
with open("arrays.npy", "rb") as f:
    B_loaded = np.load(f)
    C_loaded = np.load(f)
    print("B加载后的内容：")
    print(B_loaded)
    print("C加载后的内容：")
    print(C_loaded)