class Solution:
    def reverse(self, x: int) -> int:
        
        def reverse_signed(num):
            sum=0
            sign=1
            if num<0:
                sign=-1
                num=num*-1
            while num>0:
                rem=num%10
                sum=sum*10+rem
                num=num//10
            if not -2147483648<sum<2147483647:
                return 0
            return sign*sum
        return reverse_signed(x)