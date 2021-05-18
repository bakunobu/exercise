from typing import Union


def insert_two_nums(nums:list, n:Union[int, float],
                    m:Union[int, float]) -> list:
    n_ind = [i for i in range(nums) if nums[i] > n]
    i = 0
    for j in range(len(n_ind)):
        n_ind[j] += i
        i += 1
    for i in n_ind:
        nums.insert(i, n)
    m_ind = [i for i in range(nums) if nums[i] > m]
    i = 1
    for j in range(len(m_ind)):
        m_ind[j] += i
        i += 1
    for i in m_ind:
        nums.insert(i, m)
    return(nums)