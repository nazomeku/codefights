"""Given a list of courses, remove the courses with titles consisting of
x letters and return the result."""


def college_courses(x, courses):
    def should_consider(course):
        return len(course) != x

    return list(filter(should_consider, courses))
