class Solution:
    def the_sum_function(self,num_list,target):
        test_list =[]
        complement_dict = dict()
        for e in range(len(num_list)):
            test_list.append((e,target-num_list[e]))
            print(test_list)

        # for x,y in test_list:
        #     if x in complement_dict:
        #         return(test_list.index(x),)
        



s=Solution()
print(s.the_sum_function([3,2,4],6))





