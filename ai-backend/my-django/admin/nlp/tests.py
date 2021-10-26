from django.test import TestCase
from collections import defaultdict

# Create your tests here.
from admin.nlp.models import NaverMovie

if __name__ == '__main__':
    n = NaverMovie()
    n.model_fit()
    n.classify('내 인생 최고의 영화')


    '''
        # 방법 range()
        dc1 = {}
        dc2 = {}
        dc3 = {}
        dc4 = defaultdict(lambda: [0, 0])
        ls1 = ['10', '20', '30', '40', '50']
        ls2 = [10, 20, 30, 40, 50]
        # for i in range(0, len(ls1)):
        #     dc1[ls1[i]] = ls2[i]
    
        dc1.update({ls1[i]: ls2[i] for i in range(0, len(ls1))})
    
        # 방법 zip()
        # for i, j in zip(ls1, ls2):
        #     dc2[i] = j
    
        dc2 = {i: j for i, j in zip(ls1, ls2)}
    
        # 방법 enumerate()
        # for i, j in enumerate(ls2):
        #     dc3[j] = ls2[i]
    
        dc3 = {j: ls2[i] for i, j in enumerate(ls1)}
    
    
        for i, j in zip(ls1, ls2):
            dc4[i][1] = j
        print(f'dc4 : \n {dc4}')
    
        for i, j in enumerate(ls1):
            dc4[j][0] = j
            # defaultdict( < function <lambda > at 0x000001B44581C550 >,
            # {'10': ['10', 10], '20': ['20', 20], '30': ['30', 30], '40': ['40', 40], '50': ['50', 50]})
            # dc4[i][0] = j
            # defaultdict(<function <lambda> at 0x0000021EFEA4C550>,
            # {'10': [0, 10], '20': [0, 20], '30': [0, 30], '40': [0, 40], '50': [0, 50], 0: ['10', 0], 1: ['20', 0], 2: ['30', 0], 3: ['40', 0], 4: ['50', 0]})
    
        print('*' * 30)
        print(f'dc1 : \n {dc1}')
        print('*' * 30)
        print(f'dc2 : \n {dc2}')
        print('*' * 30)
        print(f'dc3 : \n {dc3}')
        print('*' * 30)
        print(f'dc4 : \n {dc4}')
        print('*' * 30)
    '''
