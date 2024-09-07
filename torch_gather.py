import torch
a = torch.Tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15]]).to(torch.int64)
index = torch.Tensor([[0,3,2]]).to(torch.int64)

print('a.shape: ',a.shape)
print('index.shape: ',index.shape)
print(torch.gather(a, dim=1,index =index.permute(1,0)))

print(torch.Tensor(2,2).fill_(True).to(torch.bool))
print(index.size(0))