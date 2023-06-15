import re
import ast
import json

# Function takes betti column (string) from mitDB.csv and returns
# a list with two lists inside - H0 and H1 betti


def fix_betti_string_mitdb(retarded_string):
    string_data = retarded_string[1:-1]
    string_data = (re.sub(r'\s+', ',', string_data.replace("\n", ""))).replace("[,", "[")

    # Both of these work:
    # return json.loads(string_data)
    return ast.literal_eval(string_data)


# Function takes H0 or H1 betti string from svDB.csv and returns
# a list of numbers corresponding to that string
def fix_betti_string_svdb(retarded_string):
    string_data = (re.sub(r'\s+', ',', retarded_string.replace("\n", ""))).replace("[,", "[")

    # Both of these work:
    # return json.loads(string_data)
    return ast.literal_eval(string_data)
