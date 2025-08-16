# PyTorch CUDA Extension Learning

This repository focuses on learning PyTorch CUDA extensions and exploring related debugging techniques, developed on Ubuntu 24.04 LTS with VSCode and the NVIDIA Nsight Visual Studio Code Edition extension.

## Environment

- **OS**: Ubuntu 24.04 LTS
- **PyTorch**: torch==2.7.1+cu128 (CUDA 12.8)
- **IDE**: VSCode with NVIDIA Nsight Visual Studio Code Edition
- **Python**: 3.10

## References

This project is based on and inspired by:

- **Repository**: [kwea123/pytorch-cppcuda-tutorial](https://github.com/kwea123/pytorch-cppcuda-tutorial)
- **Video Tutorial**: [PyTorch C++/CUDA Extension Tutorial](https://www.youtube.com/watch?v=l_Rpk6CRJYI&list=PLDV2CyUo4q-LKuiNltBqCKdO9GH4SS_ec)

## Updates and Modifications

Since the original repository and videos were created 3 years ago, PyTorch and CUDA APIs have been updated. This repository includes:

- **Updated code** to work with current PyTorch/CUDA APIs
- **Fixed deprecated functions** and compatibility issues
- **Added debugging capabilities** and related code
- **Comprehensive debugging workflow** documentation

## Project Structure

```
├── cpplearning/              # Working CUDA extension code
│   ├── cppcuda_tutorial.*    # Main extension (working version)
│   └── .vscode/              # VSCode configuration for main project
├── cpplearning_debug/        # Debug-enabled version
│   ├── cppcuda_tutorial_1.*  # Debug extension version
│   └── .vscode/              # VSCode configuration for debugging
├── requirements_cppcuda.txt  # pip requirements
├── environment_cppcuda.yml   # conda environment file
└── cpplearning_debug.txt     # Debugging workflow and issues encountered
```

### Extensions

- **cppcuda_tutorial**: Main working extension for normal execution
- **cppcuda_tutorial_1**: Debug-enabled version for development and troubleshooting

## Environment Setup

### Option 1: Using conda environment file (Recommended)

```bash
conda env create -f environment_cppcuda.yml
conda activate cppcuda
```

### Option 2: Using pip requirements

```bash
conda create -n cppcuda python=3.10
conda activate cppcuda
pip install -r requirements_cppcuda.txt
```

## Important Notes

⚠️ **Before running any code in this repository**, you must:

1. **Update VSCode configuration**: Modify the JSON files in the `.vscode/` folders to match your system's environment paths
2. **Check CUDA compatibility**: Ensure your CUDA installation is compatible with PyTorch 2.7.1+cu128 (CUDA 12.8)
3. **Verify paths**: Update any hardcoded paths in the configuration files to match your setup

## Debugging

For detailed debugging workflow and common issues encountered during development, please refer to:

- `cpplearning_debug.txt` - Contains debugging steps and solutions to common problems

## Building and Running

1. Navigate to either `cpplearning/` or `cpplearning_debug/` directory
2. Build the extension:
   ```bash
   python setup.py build_ext --inplace
   ```
3. Run the test:
   ```bash
   python test.py
   ```

## Debugging with VSCode + Nsight

The `cpplearning_debug/` folder is specifically configured for debugging CUDA kernels using VSCode with NVIDIA Nsight Visual Studio Code Edition. Make sure to:

1. Install NVIDIA Nsight Visual Studio Code Edition
2. Update the launch configuration in `.vscode/launch.json`
3. Set appropriate breakpoints in your CUDA code
4. Use the debug version (`cppcuda_tutorial_1`) for debugging sessions

## Acknowledgments

Special thanks to [kwea123](https://github.com/kwea123) for the original tutorial and codebase that served as the foundation for this learning project.

---

**Hope this repository helps you in your CUDA extension development journey! Thank you!** 🚀
