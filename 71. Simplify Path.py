class Solution:
    def simplifyPath(self, path: str) -> str:
        hashmap = {}
        while path[-1] == "/":
            path = path[:-1]
        while "//" in path:
            path = path.replace("//", "/")
        while "..." in path:
            for p in range(0, len(path), 3):
                if path[p:p + 3] == "...":
                    dots = 0
                    while p < len(path) and path[p] == ".":
                        dots += 1
                        p += 1
                    hashmap[f"{dots}__NAME__"] = dots
                    path = path.replace("." * dots, f"{dots}__NAME__")
                    break
        # path = path[::-1]
        while ".." in path:

            print(path)
            quit()
        for key, val in hashmap.items():
            path = path.replace(key, "." * val)
        return path


if __name__ == '__main__':
    print(Solution().simplifyPath("/a/./b/../../c/"))
