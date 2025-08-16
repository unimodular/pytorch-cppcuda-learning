import glob
import os.path as osp
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

ROOT_DIR = osp.dirname(osp.abspath(__file__))
include_dirs = [osp.join(ROOT_DIR, "include")]

sources = glob.glob('*.cpp')+glob.glob('*.cu')


setup(
    name='cppcuda_tutorial_1',# NOTE: 这个是到时候在python调用的名称
    version='2.0',
    author='kwea123',
    author_email='kwea123@gmail.com',
    description='cppcuda_tutorial',
    long_description='cppcuda_tutorial',
    ext_modules=[
        CUDAExtension(
            name='cppcuda_tutorial_1',
            sources=sources,# NOTE: 这个是要build的C++,cuda文件
            include_dirs=include_dirs,
            extra_compile_args={
                            'cxx': ['-g'], # 为C++代码也加上调试信息
                            'nvcc': ['-g', '-G'] # 为CUDA代码加上调试信息
                        }
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)


# 这段代码是用来编译和安装自定义 C++/CUDA 扩展到 PyTorch 的 Python 包。主要作用如下：

# 导入了 setuptools 和 PyTorch 的扩展工具。
# setup(...) 是打包和安装的入口，参数说明：
# name：包的名字，安装后在 Python 里用这个名字导入。
# version、author、description 等是包的元信息。
# ext_modules：指定要编译的扩展模块，这里用 CUDAExtension（即使只有 C++ 也可以用），
# name：扩展模块的名字（Python 导入时用）。
# sources：要编译的 C++ 源文件列表。
# cmdclass：指定 build_ext 命令用 PyTorch 的 BuildExtension，支持 CUDA/C++ 编译。
# 总结：这段代码让你可以用 python setup.py install 或 pip install . 来编译并安装你的 C++/CUDA 扩展，之后在 Python 里直接 import 并调用。
