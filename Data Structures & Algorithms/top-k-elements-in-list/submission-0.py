class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}

        for num in nums:

            if num not in d:
                d[num]=1

            else:
                d[num]+=1

        bucket=[[] for _ in range (len(nums)+1) ]

        for num in d:
            count=d[num]
            bucket[count].append(num)

        ans=[]

        for i in range (len(bucket)-1,-1,-1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans)==k:
                    return ans