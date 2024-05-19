from datetime import datetime

def sort_assignments_by_deadline(assignments):
    assignments.sort(key=lambda x: x['deadline'])
    return assignments

if __name__ == "__main__":
    assignments = [
        {'title': 'Math Homework', 'deadline': '2024-06-01'},
        {'title': 'Science Project', 'deadline': '2024-05-20'},
        {'title': 'History Essay', 'deadline': '2024-05-25'},
        {'title': 'Art Presentation', 'deadline': '2024-06-10'}
    ]


    sorted_assignments = sort_assignments_by_deadline(assignments)
    
    print("과제 제출 일정:")
    for assignment in sorted_assignments:
        print(f"{assignment['title']} - 마감일: {assignment['deadline']}")