#mean

num=[1,2,3,4,5]
sum=len(num)
a=0
for i in num:
    a=a+i
mean=(a/sum)
print(mean)

#median

num=[1,2,3,4,5,6,7]
sum=len(num)
guru=(int(sum/2))
print(num[guru])

#standard deviation

x=[1,2,3,4,5,1,1,1]
y=0
for i in range(len(x)):
    y=y+((x[1]-mean)**2)
sd=(y/len(x))**0.5
print("standard deviation:",round(sd,2))

#mode

a=[1,2,3,4,5,6,3,3,3,2]
x=0
y=a[0]
for i in a:
    don = a.count(i)
    if don>x:
        x=don
        y=i
print("mode",y)
