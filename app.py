TASKS = [
    {"title": "주간 보고서 초안 작성", "priority": "HIGH", "done": False},
    {"title": "회의 자료 작성", "priority": "MID", "done": False},
    {"title": "책상 정리", "priority": "LOW", "done": False},
    {"title": "이메일 답장", "priority": "HIGH", "done": True},
]

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}


def pending_tasks(tasks):
    # sorted()는 안정 정렬이라 우선순위가 같으면 적은 순서가 유지된다.
    pending = [t for t in tasks if not t["done"]]
    return sorted(pending, key=lambda t: PRIORITY_ORDER[t["priority"]])


def main():
    for task in pending_tasks(TASKS):
        print(f"{task['title']} ({task['priority']})")


if __name__ == "__main__":
    main()
