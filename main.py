
def check_cuda():
    import torch

    if torch.cuda.is_available():
        print(f"Using CUDA. Version: {torch.version.cuda}")
    else:
        print("CUDA is not available")

def check_system():
    """
    Prints available resources.
    :return: None
    """
    import torch
    import os

    print('Total CPUs (threads) found:',os.cpu_count())
    print('Available threads for torch:',torch.get_num_threads())

    if torch.cuda.is_available():
        count = torch.cuda.device_count()
        print('Total GPUs found:',str(count))
        for i in range(torch.cuda.device_count()):
            print(i, torch.cuda.get_device_name(i), torch.cuda.get_device_properties(i))
    else:
        print('No GPUs found!')

if __name__ == '__main__':
    check_cuda()
    check_system()

