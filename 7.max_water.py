arr =[1,8,6,2,5,4,8,3,7]
left =0
right = len(arr)-1
max_area = 0

while left<right:
    curr_height_of_contianer = min(arr[left],arr[right])
    curr_area = curr_height_of_contianer*(right-left)
    max_area = max(curr_area,max_area)

    if arr[left]<arr[right]:
        left = left+1
    else: right = right-1

print(max_area)