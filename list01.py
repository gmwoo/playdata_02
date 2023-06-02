# 리스트 - 배열, 하나의 메모리에 여러개의 데이터 저장 가능
nums = [1,2,3,4,5,6,7,8,9]
print(nums)
print(nums[0]) # 0번 방의 데이터만, 이것을 인덱싱이라고 함

nums[0] = [10] # 인덱싱을 이용한 값 변경
nums[1] = [20]
nums[2] = 30
print(nums)

# 위의 리스트 nums의 값들은 제거되고 새로운 값으로 저장
nums = [10, 20, 30] # 새로 메모리를 만들어서 10, 20, 30을 저장하므로 위의 리스트 사라짐
print(nums)

# 반복 처리
for n in nums:   # for 변수명 in 리스트타입 -> 데이터 차례대로 하나씩 옮김
    print(n)