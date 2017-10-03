"""Return true if the scholarships are correctly distributed
and false otherwise."""


def correct_scholarships(best_students, scholarships, all_students):
    return set(best_students) <= set(scholarships) < set(all_students)
