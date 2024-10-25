import torch
import numpy as np

class CreateTensors:
    def __init__(self) -> None:
        '''torch.zeros: 创建全零矩阵, torch.ones: 创建全一矩阵
        torch.rand: 创建随机矩阵（均匀分布), torch.randn: 创建随机矩阵（正态分布）'''
        self.generate_by_shape_indicate = {'0': torch.zeros, '1': torch.ones, \
                             '2':torch.rand,'3':torch.randn}
        
    def create_tensor_by_shape(self, shape, indicate=0):
        if isinstance(indicate, int):
            result_tensor = self.generate_by_shape_indicate[str(indicate)](shape)
        elif isinstance(indicate, str):
            result_tensor = self.generate_by_shape_indicate[indicate](shape)
        return result_tensor

    def create_tensors_by_list(self, shape, lst=[[1, 2, 3], [4, 5, 6]]):
        '''lst: a list of any shape'''
        tensor1 = torch.tensor(lst)
        # 使用 NumPy 数组创建矩阵
        arr = np.array(lst)
        tensor2 = torch.from_numpy(arr)
        # 创建全零矩阵
        tensor3 = torch.zeros(2, 3)
        # 创建全一矩阵
        tensor4 = torch.ones(2, 3)
        # 创建随机矩阵（均匀分布）
        tensor5 = torch.rand(2, 3)
        # 创建随机矩阵（正态分布）
        tensor6 = torch.randn(2, 3)
        # 创建与指定矩阵形状相同的全零矩阵
        tensor7 = torch.zeros_like(tensor1)
        # 创建与指定矩阵形状相同的全一矩阵
        tensor8 = torch.ones_like(tensor1)
        # 创建与指定矩阵形状相同的随机矩阵（均匀分布）
        tensor9 = torch.rand_like(tensor1)
        # 创建与指定矩阵形状相同的随机矩阵（正态分布）
        tensor10 = torch.randn_like(tensor1)
        tensor_result = tensor1
        return tensor_result

create_tensor = CreateTensors()
tensor_example = create_tensor.create_tensor_by_shape((2,3),0)
print(tensor_example)
print(tensor_example.data)
