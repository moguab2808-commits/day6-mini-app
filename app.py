import argparse

TASKS = [
    {"title": "주간 보고서 초안 작성", "priority": "HIGH", "done": False},
    {"title": "회의 자료 작성", "priority": "MID", "done": False},
    {"title": "책상 정리", "priority": "LOW", "done": False},
    {"title": "이메일 답장", "priority": "HIGH", "done": True},
]

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}


def sorted_tasks(tasks, include_done=False):
    # sorted()는 안정 정렬이라 우선순위가 같으면 적은 순서가 유지된다.
    shown = [t for t in tasks if include_done or not t["done"]]
    return sorted(shown, key=lambda t: PRIORITY_ORDER[t["priority"]])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="완료한 일도 함께 보여 준다")
    args = parser.parse_args()

    for task in sorted_tasks(TASKS, include_done=args.all):
        suffix = " (완료)" if task["done"] else ""
        print(f"[{task['priority']}] {task['title']}{suffix}")


if __name__ == "__main__":
    main()
