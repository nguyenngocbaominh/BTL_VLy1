
nums1=[1,2]
nums2=[3,4]

merge=sorted(nums1+nums2)
print(merge)
length=len(merge)
if length%2==0: 
    mot=(length//2)
    hai=mot-1
    a=float((merge[hai]+merge[mot])/2)
elif length==0:
    a=0
else:
    a=merge[(length-1)/2]
print(a)
