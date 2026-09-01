import argparse
from pathlib import Path

def main(arv=None):
    return 0

"""
# add task
lern tasks add "Buy groceries" --priority high

# list tasks
lern tasks list
# mark task done
lern tasks done 1
# delete task
lern tasks delete 1
# filter by status or priority
lern tasks list --status open
lern tasks list --priority high
# save/load tasks from disk 
"""

"""
data model object
id: int
title: str
description: str or empty
status: str (open, done)
priority: str (low, medium, high)
due_date: str or empty
created_at: str (timestamp)
completed_at: str or empty (timestamp)
"""

"""
optional features:
- priority filtering
- due date filtering
- search by title or description
- show "open tasks only" by default
"""

if __name__ == "__main__":
    raise SystemExit(main())