
from bisect import bisect_left


def lengthOfLIS(nums: list[int]) -> int:
    if not nums:
        return 0

    tails = []

    for num in nums:
        # Find the first element >= current number
        index = bisect_left(tails, num)

        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num

    return len(tails)


def main():
    try:
        nums = list(map(
            int, input("Enter array elements: ").split()
        ))

        result = lengthOfLIS(nums)

        print("Input Array:", nums)
        print("Length of Longest Increasing Subsequence:", result)

    except ValueError:
        print("Error: Enter valid integers only.")


if __name__ == "__main__":
    main()
