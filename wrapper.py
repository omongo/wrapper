class Wrapper:
    @staticmethod
    def wrap(s, col):
        """ (str, int) -> str
        Return the string (s), but with line breaks inserted at just the right
        places to make sure that no line is longer than the column number (col).
        """
        if len(s) <= col:
            return s
        i = s.rfind(' ', 0, col)
        if i == -1:
            return s[:col] + '\n' + Wrapper.wrap(s[col:], col)
        else:
            return s[:i] + '\n' + Wrapper.wrap(s[i+1:], col)
