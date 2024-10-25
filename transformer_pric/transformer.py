import torch
import torch.nn as nn
import numpy as np

class MultiHeadAttention(nn.Model):
    def __init__(self, embedding_dim, num_head, hidden_dim, bias):
        '''input is [batch, sql, embed_dim]'''
        self.embedding_dim = embedding_dim
        self.num_head = num_head
        self.hidden_dim = hidden_dim
        self.q_proj = nn.linear(embedding_dim, hidden_dim*num_head,bias=bias)
        self.k_proj = nn.linear(embedding_dim, hidden_dim*num_head,bias=bias)
        self.v_proj = nn.linear(embedding_dim, hidden_dim*num_head,bias=bias)
        self.o_proj = nn.linear(hidden_dim*num_head, hidden_dim*num_head,bias=bias)

    def get_attention_mask(self, seq):
        atten_shape = seq.size()

    def forward(self, q, k, v, atten_mask):
        query = self.q_proj(q)
        key = self.k_proj(k)
        value = self.v_proj(v)
        attention_ = query@key.transport(-1,-2)
        atttention_ = nn.sorftmax()


if __name__=='__main__':
    '''input data: [batchsize, seq_length, ]'''
    # 使用列表创建矩阵
    lst = [[1, 2, 3], [4, 5, 6]]
    tensor1 = torch.tensor(lst)

    # 使用 NumPy 数组创建矩阵
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    tensor2 = torch.from_numpy(arr)


