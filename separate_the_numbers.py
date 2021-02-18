def is_subnumber_beautiful(prev_number: int, subnumber_as_string: str) -> bool:
    if len(subnumber_as_string) == 0:
        return True
    if subnumber_as_string[0] == "0":
        return False
    for i in range(1, len(subnumber_as_string) + 1):
        next_number = subnumber_as_string[0:i]
        if int(next_number) == prev_number + 1:
            return is_subnumber_beautiful(int(next_number), subnumber_as_string[i:])
    return False


def separateNumbers(number_as_string: str) -> None:
    for i in range(1, len(number_as_string)):
        prev_number = int(number_as_string[0:i])
        subnumber_as_string = number_as_string[i:]
        if is_subnumber_beautiful(prev_number, subnumber_as_string):
            print(f"YES {prev_number}")
            return
    print("NO")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
