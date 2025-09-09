def compare_strings(str1, str2):
    # Write code here
    return {
        "is_substring":str1 in str2,
        "starts_with":str2.startswith(str1),
        "ends_with":str2.endswith(str1),
        "is_equal":str1.lower()==str2.lower(),
    }