def solution(string,markers):
    ls = string.split("\n")
    for m in markers:
        ls = [v.split(m)[0].rstrip() if m in v else v for v in ls]
    return "\n".join(ls)
