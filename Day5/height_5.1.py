# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
totalheight=0
cnt=0
for height in student_heights:
    totalheight+=height
    cnt+=1
avg_height=int(totalheight/cnt)
print(avg_height)
#Write your code below this row 👇

