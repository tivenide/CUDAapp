
def check_cuda():
    import torch

    if torch.cuda.is_available():
        print(f"Using CUDA. Version: {torch.version.cuda}")
    else:
        print("CUDA is not available")

if __name__ == '__main__':
    check_cuda()

