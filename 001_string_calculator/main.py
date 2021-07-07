from re import finditer


def add(numbers: str) -> int:
    if numbers:
        # not empty string

        # set defaults
        default_delimiter = ','
        delimiters = ['\n']
        my_sum = 0
        negatives = []
        last_close_square_b = 0

        # read optional delimiter
        if numbers.startswith('//'):  # delimiter is defined
            # check if delimiter is defined in square braces
            # find all open square braces
            for match in finditer('\[', numbers):
                # find immediate close brace
                start = match.start()
                close = numbers[start:].find(']') + start  # +start because start was beginning of searched string

                # save close as last one
                last_close_square_b = close

                # append delimiter to delimiters
                delimiters.append(numbers[start+1:close])

            if last_close_square_b:
                # delimiter(s) in square brace(s)
                # delete delimiter section from numbers string
                numbers = numbers[last_close_square_b + 2:]  # +1 for ] and +1 for \n

            else:
                # delimiter not in square brace
                delimiters.append(numbers[2])
                # delete delimiter section from numbers string
                numbers = numbers[4:]

        # replace delimiters with default delimiter
        for d in delimiters:
            numbers = numbers.replace(d, default_delimiter)

        # now split by default delimiter
        integer_nums = numbers.split(default_delimiter)

        for num in integer_nums:
            # convert number to integer and strip white spaces
            num = int(num.strip())

            if num < 0:
                # number is negative add to negatives list
                negatives.append(num)

            else:
                # number is positive add to my_sum if it's less than 1001
                if num < 1001:
                    my_sum += num

        # check if we have negative numbers
        if negatives:
            raise Exception(f"negatives not allowed {negatives}")
        return my_sum
    # empty string
    return 0
