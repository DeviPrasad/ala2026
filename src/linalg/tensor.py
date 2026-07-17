import torch

assert torch.__version__ >= "2.0.0", "Requires PyTorch 2.0.0 or higher"

# rank-zero tensor is a scalar, it has no dimensions, and its shape is an empty tuple ()
def test_rank0_tensor_shapes():
    a = torch.rand(())
    assert a.dtype == torch.float32
    assert a.shape == ()
    assert a.dim() == 0
    assert a.ndim == 0
    #
    a = torch.tensor(10)
    assert a.dtype == torch.int64
    assert a.shape == ()
    assert a.dim() == 0
    assert a.ndim == 0
    #
    a = torch.tensor(1024, dtype=torch.int16)
    assert a.dtype == torch.int16
    assert a.shape == ()
    assert a.dim() == 0
    assert a.ndim == 0

# a = [a0, a1, a2]
def test_rank1_tensor_shapes():
    a = torch.rand(3)
    assert a.dtype == torch.float32
    assert a.shape == (3,)
    assert a.dim() == 1
    assert a.ndim == 1
    assert a[0].shape == ()
    assert a[1].shape == ()
    assert a[2].shape == ()

# a = [[a0, a1, a2]]
def test_rank2_tensor_shapes_01():
    a = torch.rand(1, 3)
    assert a.dtype == torch.float32
    assert a.shape == (1, 3)
    assert a.dim() == 2
    assert a.ndim == 2
    ##
    assert a[0].shape == (3,)
    assert a[0].ndim == 1
    assert a[0].dim() == 1
    assert a[0][0].shape == ()

# a = [[a0, a1, a2], [b0, b1, b2]]
def test_rank2_tensor_shapes_02():
    a = torch.rand((2, 3))
    assert a.dtype == torch.float32
    assert a.shape == (2, 3)
    assert a[0].shape == (3,)
    assert a[1].shape == (3,)
    assert a[1:].shape == (1, 3)
    #
    a[1, 0] = 4
    a[1, 1] = 5
    a[1, 2] = 6
    #
    exp = torch.tensor([4, 5, 6], dtype=torch.int16)
    assert exp.shape == (3,)
    assert torch.equal(a[1], exp)
    #
    exp = torch.tensor([[4, 5, 6]], dtype=torch.int16)
    assert torch.equal(a[1:], exp)

def test_tensor_int():
    # Create a tensor of shape (2, 3)
    a = torch.rand(2, 3)
    assert a.shape == (2, 3)

    b = torch.randint(0, 4096, (3, 3, 3), dtype=torch.int16)
    assert b.shape == (3, 3, 3)

if __name__ == "__main__":
    test_rank0_tensor_shapes()
    test_rank1_tensor_shapes()
    test_rank2_tensor_shapes_01()
    test_rank2_tensor_shapes_02()
    test_tensor_int()
