#https://leetcode.com/problems/course-schedule/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Generate adjacent list
        adjacent_dict = {course:[] for course in range(0, numCourses, 1)}
        for course in prerequisites:
            # course[0] is the current coruse and course[1] is prerequisit of the current course
            adjacent_dict[course[0]].append(course[1])
        
        # DFS 
        for course in range(numCourses):
            # reset visited course when the prerequisites of the new course are checked
            visited_courses = []
            if not self.check_pre(course, adjacent_dict, visited_courses):
                return False
        
        return True
    
    def check_pre(self, course, adjacent_dict, visited_courses):
        if course in visited_courses:
            # If the visited course has been visited again, then it means the loop
            return False
        
        # The course has been visited.
        # If the visited course has been visited again in the same DFS search, It is the loop and will return false
        visited_courses.append(course)
        
        if adjacent_dict[course]:
            # The prerequisites of a course has not been checked yet
            for pre in adjacent_dict[course]:
                # visit the prerequisites
                if self.check_pre(pre, adjacent_dict, visited_courses):
                    # If the prerequisites of the certain course can be completed, 
                    # it will be removed from the current course. By doing so,
                    # this pre-course do not need to be checked again in other course check if a course is required by
                    # several courses. 
                    adjacent_dict[course].remove(pre)
                else:
                    return False
                
        # The current course check finishes, so remove it from the visited list. 
        # The other DFS from other vetices/courses may visit/need this course again
        visited_courses.remove(course)
        return True

def main():
    numCourses = 2
    prerequisites = [[1,0]]
    result = Solution().canFinish(numCourses, prerequisites)
    print(result)


if __name__ == '__main__':
    main()