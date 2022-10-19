arr = ['abc', 'bc', 'def', 'abc', 'bc', 'ccc', 'bc']
prev = set(arr[0])
res = [arr[0]]
for i in range(1, len(arr)):
        curr = set(arr[i])
        if prev >= curr:
                res.append(arr[i])
        else:
                if len(res) > 1:
                    print(res)
                res = [arr[i]]
        prev = curr




