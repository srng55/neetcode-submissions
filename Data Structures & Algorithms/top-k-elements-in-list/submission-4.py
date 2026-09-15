class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}

        for num in nums:

            count[num]=count.get(num,0)+1

        bucket=[[] for _ in range (len(nums)+1) ]

        for num,count in count.items():
            
            bucket[count].append(num)

        ans=[]

        for i in range (len(bucket)-1,-1,-1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans)==k:
                    return ans