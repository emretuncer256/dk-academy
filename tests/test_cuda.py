import torch


def test_cuda_availability():
    assert torch.cuda.is_available(
    ), "CUDA is not available. Please ensure that your system has a CUDA-capable GPU and the correct drivers installed."
