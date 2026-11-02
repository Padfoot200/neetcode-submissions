class Solution:
    def isHappy(self, n: int) -> bool:
        current_num_str=str(n)
        num_set=set()
        sum_digits_sqrd= 0
        while( 1 not in num_set):
            for digit in current_num_str:
                sum_digits_sqrd += int(digit)**2
            if(sum_digits_sqrd not in num_set):
                print("this iteration sum", sum_digits_sqrd)
                num_set.add(sum_digits_sqrd)
            
            else:
                return False
            current_num_str=str(sum_digits_sqrd)
            sum_digits_sqrd= 0
        return True