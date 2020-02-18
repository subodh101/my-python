def clean_up(text_not_allowed, raw_string):
    """
    str.maketrans takes two arguments of input and output string of same length
    for mapping input to put output

    In our case we are mapping each character to None.
    Args:
        text_not_allowed: string with characters that are not allowed
        raw_string: string that needs to be cleaned up

    Returns: clean string after removal of the not allowed characters

    """
    trans_table = str.maketrans(dict.fromkeys(text_not_allowed))
    clean_result = raw_string.translate(trans_table)
    return clean_result


def main():
    not_allowed = "~`!@#$%^&*()_+-={}[]\|:;'<,>/?"
    raw_string = "!#$t!h!@$#$^@#%/(*)&^(%i!$%s &`lo@#o%k(*^&s *^&%:p!@%@!%yt$%*^&ho&(*^n(*)_ic *()_to !@#$m@$#e.!@$#@#!%$#^%&^*&(*)'"
    print("input:\n", raw_string)
    result = clean_up(text_not_allowed=not_allowed, raw_string=raw_string)
    print("output:\n", result)


if __name__ == '__main__':
    main()
