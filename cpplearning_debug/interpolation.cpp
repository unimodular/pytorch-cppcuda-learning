#include <torch/extension.h>

#include "include/utils.h"

// torch::Tensor trilinear_interpolation(
//     torch::Tensor feats,
//     torch::Tensor points)
std::vector<torch::Tensor> trilinear_interpolation(
    torch::Tensor feats,
    torch::Tensor points)
{
    CHECK_INPUT(feats);
    CHECK_INPUT(points);
    // NOTE: 这里的 CHECK_INPUT() 宏会检查 feats 和 point 是否是 CUDA 张量且是连续的。
    return trilinear_fw_cu(feats, points);
}

// NOTE: 简单理解：这个函数接收两个张量，返回第一个张量。语法结构为：返回类型 函数名(参数列表) { 函数体 }。

/*
torch::Tensor：这是函数的返回类型，表示返回一个张量（PyTorch 的数据结构）。
trilinear_interpolation：这是函数名。
torch::Tensor feats, torch::Tensor point：这是函数的参数列表，表示输入两个张量。
{ return feats; }：这是函数体，表示函数执行时会直接返回输入的 feats 参数。
*/

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m)
{
    m.def("trilinear_interpolation", &trilinear_interpolation);
}

// NOTE: 这个是python认识C++的桥梁。这段代码让 Python 能直接调用 C++ 的 trilinear_interpolation，用于高性能计算或与 PyTorch 深度集成