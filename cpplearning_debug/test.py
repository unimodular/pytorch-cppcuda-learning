import torch

import cppcuda_tutorial_1

import time

# feats = torch.ones(2)
# points = torch.zeros(2)

# out = cppcuda_tutorial_1.trilinear_interpolation(feats, points)

# print(out)
def trilinear_interpolation_py(feats, points):
    """
    Inputs:
        feats: (N, 8, F)
        points: (N, 3) local coordinates in [-1, 1]
    
    Outputs:
        feats_interp: (N, F)
    """
    u = (points[:, 0:1]+1)/2
    v = (points[:, 1:2]+1)/2
    w = (points[:, 2:3]+1)/2
    a = (1-v)*(1-w)
    b = (1-v)*w
    c = v*(1-w)
    d = 1-a-b-c

    feats_interp = (1-u)*(a*feats[:, 0] +
                          b*feats[:, 1] +
                          c*feats[:, 2] +
                          d*feats[:, 3]) + \
                       u*(a*feats[:, 4] +
                          b*feats[:, 5] +
                          c*feats[:, 6] +
                          d*feats[:, 7])
                          
    feats_interp2 = (2-u)*(a*feats[:, 0] +
                          b*feats[:, 1] +
                          c*feats[:, 2] +
                          d*feats[:, 3]) + \
                       u*(a*feats[:, 4] +
                          b*feats[:, 5] +
                          c*feats[:, 6] +
                          d*feats[:, 7])
    
    return feats_interp, feats_interp2

if __name__ == "__main__":
    N = 65536
    F = 256
    # feats = torch.ones(3, device='cuda')  # 创建一个在 CUDA 上的张量
    # points = torch.zeros(2, device='cuda')  # 创建一个在 CUDA 上的张量
    feats = torch.rand(N, 8, F, device='cuda') 
    points = torch.rand(N, 3, device='cuda') * 2 - 1  # 随机生成范围在 [-1, 1] 的 CUDA 张量

    # print("feats shape:", feats.shape)  # 输出形状以验证
    # print("points shape:", points.shape)
    
    # # feats = feats.cuda()  # 将张量转移到 CUDA
    # # points = points.cuda()  # 如果 points 也需要在 CUDA 上
    # t = time.time()
    # result_py = trilinear_interpolation_py(feats, points)
    # print(f"pytorch_time: {time.time() - t:.6f} seconds")
    # feat_interp_py, feat_interp2_py = result_py
    # print('feat_interp_py:', feat_interp_py)
    # print('feat_interp2_py:', feat_interp2_py)
    t = time.time()
    result_cuda = cppcuda_tutorial_1.trilinear_interpolation(feats, points)
    print(f"cuda_time: {time.time() - t:.6f} seconds")
    print("Result shape:", [r.shape for r in result_cuda])  # 输出结果的形状
    feat_interp_cuda, feat_interp2_cuda = result_cuda
    # print("feat_interp_cuda:", feat_interp_cuda)
    # print("feat_interp2_cuda:", feat_interp2_cuda)

    # start = time.time()
    # for _ in range(1000):
    #     out = cppcuda_tutorial_1.trilinear_interpolation(feats, points)
    # end = time.time()
    # print(f"Average time: {(end - start) / 1000:.6f} seconds")
    # print("Output:", out)
    # print(torch.allclose(result_py[0],result_cuda[0], atol=1e-6))