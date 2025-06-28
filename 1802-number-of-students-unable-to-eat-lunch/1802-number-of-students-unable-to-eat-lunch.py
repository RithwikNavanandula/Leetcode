class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while sandwiches:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                if sandwiches[0] in students:
                    students = students[1:]+[students[0]]
                else:
                    break
        return len(students)