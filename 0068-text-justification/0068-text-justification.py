class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        p = []  
        s = []  

        for i in range(len(words)):
            if sum(len(w) for w in s) + len(words[i]) + len(s) <= maxWidth:
                s.append(words[i])
            else:
                p.append(s)
                s = [words[i]]
        if s:
            p.append(s)
        w = []  
        for line in p[:-1]:  
            if len(line) == 1:
                justified = line[0] + ' ' * (maxWidth - len(line[0]))
            else:
                total_chars = sum(len(word) for word in line)
                spaces_needed = maxWidth - total_chars
                gaps = len(line) - 1
                even_space = spaces_needed // gaps
                extra_space = spaces_needed % gaps

                justified = ''
                for i in range(gaps):
                    justified += line[i]
                    justified += ' ' * (even_space + (1 if i < extra_space else 0))
                justified += line[-1]

            w.append(justified)
        last_line = ' '.join(p[-1])
        last_line += ' ' * (maxWidth - len(last_line))
        w.append(last_line)

        return w
