#include<stdio.h>

int removeDuplicates(int* nums, int numsSize) {
  int i,j,k=0;
  
  while (i<numsSize){
      while(nums[i+1] == nums[i])
        i++;
      i++;
      k++;
      nums[k-1]=nums[i-1];
      
  }
  nums[k]='\0';
  return nums;
}

int main(){
  int nums[6] = {1,1,1,2,2,3};
  int a = removeDuplicates(nums,6);
  for(int i=0;i<3;i++)
    printf("%d",nums[i]);
}