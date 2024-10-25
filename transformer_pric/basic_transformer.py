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
    def get_padding_mask(q, k, indicate_id):
        ''' seq_q: [batch, seq_len]
            seq_k: [batch, seq_len]
            return:
            mask: [batch, len_q, len_k]
        '''
        batch_size, q_length = q.size()
        batch_size, k_length = k.size()
        #pad_mask = ~(k == pad_token_id)
        pad_mask = k.eq(indicate_id).unsqeeeze(1)
        pad_mask=pad_mask.expand(batch_size, q_length, k_length)
        return pad_mask
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

