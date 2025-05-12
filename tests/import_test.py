import pytest 

def test_import():
    import torch
    x = torch.zeros(2, 3)
    print(x+1)
    assert True
