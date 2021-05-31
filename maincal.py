import add_work
import div_work
import mul_work
import sub_work

a=100
b=50

total_sum=add_work.add(a,b)
total_sub=sub_work.sub(a,b)
total_mul=mul_work.mul(a,b)
total_div=div_work.div(a,b)

print(f"Total Sum is {total_sum}. Total Sub is {total_sub}. Total Mul is {total_mul}. Total div is {total_div}.")