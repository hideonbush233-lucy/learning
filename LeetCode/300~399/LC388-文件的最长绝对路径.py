# 这里将 dir 作为根目录中的唯一目录。
# dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。

# 在文本格式中，如下所示(⟶表示制表符)：
# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
# 如果是代码表示，上面的文件系统可以写为 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 。'\n' 和 '\t' 分别是换行符和制表符。

# 文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 file2.ext 的绝对路径是 "dir/subdir2/subsubdir2/file2.ext" 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 name.extension 的格式，其中名称和扩展名由字母、数字和/或空格组成。

# 给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向文件的最长绝对路径 的长度。 如果系统中没有文件，返回 0。


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        n = len(input)
        if not input:
            return 0
        prefixSum = [0]
        res = 0
        for s in input.split('\n'):
            level = 0  # 当前层级
            while s[level] == '\t':
                level += 1
            sLen = len(s) - level
            # 如果是文件，比较最大值。
            if '.' in s:
                res = max(res, prefixSum[level] + sLen)
                continue
            # 如果是文件夹，将当前层级的字符串数目(包含末尾斜杆)保存。
            if level + 1 < len(prefixSum):
                prefixSum[level + 1] = prefixSum[level] + sLen + 1
            else:
                prefixSum.append(prefixSum[-1] + sLen + 1)
        return res
