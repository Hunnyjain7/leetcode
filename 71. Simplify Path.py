class Solution:
    # Better Approach from leetcode
    def simplifyPath(self, path: str) -> str:  # noqa
        stack = []
        for d in path.split('/'):
            if d == '':
                continue
            elif d == '..':
                if stack: stack.pop()
            elif d != '.':
                stack.append(d)
        return '/' + '/'.join(stack)

    # My solution
    def simplifyPath2(self, path: str) -> str:  # noqa
        hashmap = {}
        while path and path[-1] == "/":
            path = path[:-1]

        while "//" in path:
            path = path.replace("//", "/")

        while "..." in path:
            for p in range(0, len(path)):
                if path[p:p + 3] == "...":
                    dots = 0
                    while p < len(path) and path[p] == ".":
                        dots += 1
                        p += 1
                    hashmap[f"{dots}__NAME__"] = dots
                    path = path.replace("." * dots, f"{dots}__NAME__")
                    break
        if ".." in path.split("/"):
            path = path.split("/")
            path_copy = path.copy()
            pop_next = False
            pop_next_two = 0
            for p in range(len(path) - 1, -1, -1):
                if pop_next:
                    if path[p] == ".." or path[p] == ".":
                        if path[p] != ".":
                            pop_next_two += 1
                        path_copy.pop(p)
                    else:
                        if pop_next_two:
                            path_copy.pop(p)
                            pop_next_two -= 1
                        else:
                            # path_copy.pop(p)
                            pop_next = False
                elif path[p] == "..":
                    path_copy.pop(p)
                    pop_next_two = 1
                    pop_next = True
            path = "/".join(path_copy)

        if "." in path.split("/"):
            path = path.split("/")
            path_copy = path.copy()
            pop_next = False
            for p in range(len(path) - 1, -1, -1):
                if pop_next:
                    if path[p] == ".":
                        path_copy.pop(p)
                    else:
                        pop_next = False
                elif path[p] == ".":
                    path_copy.pop(p)
                    pop_next = True
            path = "/".join(path_copy)

        for key, val in hashmap.items():
            path = path.replace(key, "." * val)
        return path if path and path[0] == "/" else "/" + path


if __name__ == '__main__':
    # print(Solution().simplifyPath("/a/./b/../../c/"))
    # print(Solution().simplifyPath("/a/../../b/../c//.//"))
    # print(Solution().simplifyPath("/a//b////c/d//././/.."))
    print(Solution().simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/"))
    # print(Solution().simplifyPath("/..."))
