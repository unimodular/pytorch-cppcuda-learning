# debug_launcher.py
import torch
import cppcuda_tutorial_1 # <-- 导入我们刚刚用 setup.py 编译的模块

print(">>> [HOST] Python script started.")

# 1. 准备输入数据
device = torch.device("cuda:0")
feats = torch.randn(2, 8, 16, device=device, dtype=torch.float32)
# 将 points 的值范围限定在 [-1, 1]
points = torch.rand(2, 3, device=device, dtype=torch.float32) * 2 - 1 

print(">>> [HOST] Input tensors created.")

# 2. 暂停，等待我们附加调试器
print("="*50)
print(">>> [HOST] Ready to call CUDA kernel.")
print(">>> [HOST] Attach your CUDA debugger now!")
input(">>> [HOST] Press Enter to continue...") # 程序会在这里停住，直到你按回车
print("="*50)

# 3. 调用CUDA函数
print(">>> [HOST] Calling CUDA function 'trilinear_interpolation'...")
# 在 interpolation_kernel.cu 的 trilinear_fw_kernel 函数里打上断点！
outputs = cppcuda_tutorial_1.trilinear_interpolation(feats, points)
print(">>> [HOST] CUDA function finished.")

print(">>> [HOST] Output shapes:")
print(f"    - Output 1: {outputs[0].shape}")
print(f"    - Output 2: {outputs[1].shape}")