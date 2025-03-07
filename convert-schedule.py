# Description: This script converts a schedule in markdown format to an ics file.

import re
from datetime import datetime, timedelta
from icalendar import Calendar, Event

def parse_markdown_to_ics(lines, start_date):
    cal = Calendar()
    day_offset = -1

    for line in lines:
        line = line.strip()

        if line.startswith("## "):
            day_offset += 1
            continue

        if not line.startswith("| "):
            continue

        parts = line.split("|")
        if len(parts) < 3:
            continue

        time_range = parts[1].strip()
        activity = parts[2].strip()

        for segment in time_range.split("/"):
            times = re.split(r"[–-]", segment.strip())
            if len(times) < 2:
                continue

            start_str, end_str = times[0].strip(), times[1].strip()
            start_str = re.sub(r"\*\*", "", start_str)  # Remove extra characters
            end_str = re.sub(r"\*\*", "", end_str)      # Remove extra characters

            start_dt = datetime.strptime(start_str, "%H:%M")
            end_dt = datetime.strptime(end_str, "%H:%M")

            begin = start_date + timedelta(
                days=day_offset,
                hours=start_dt.hour,
                minutes=start_dt.minute
            )
            finish = start_date + timedelta(
                days=day_offset,
                hours=end_dt.hour,
                minutes=end_dt.minute
            )

            event = Event()
            event.add('summary', activity)
            event.add('dtstart', begin)
            event.add('dtend', finish)
            cal.add_component(event)

    return cal

if __name__ == "__main__":
    markdown_text = """
## **Saturday**
| **Time**         | **Activity**                                               |
|------------------|-----------------------------------------------------------|
| **09:00–12:00**  | Work on the plugin: Continue development, set up tests, and CI/CD. |
| **12:00–13:00**  | Lunch break. Short walk or light exercise.                |
| **13:00–16:00**  | Functional and technical design of the plugin.            |
| **16:00–16:30**  | Short break: Snack, stretch, or meditate.                 |
| **16:30–18:30**  | Work out use cases and develop tests according to use cases. |
| **18:30–19:30**  | Dinner and relaxation.                                    |
| **19:30–21:00**  | Work out the documentation further. Update project documentation. |
| **21:00–22:00**  | Relaxation: Hobby, show, or light reading.                |
| **22:00–23:00**  | Wind down and sleep preparation.                          |

## **Sunday**
| **Time**         | **Activity**                                               |
|------------------|-----------------------------------------------------------|
| **09:00–12:00**  | Work on database schemas and understand integration between NoSQL (Payload) and SQL (Medusa). |
| **12:00–13:00**  | Lunch break. Short walk or light exercise.                |
| **13:00–15:00**  | Continue documentation and prepare for publishing the plugin as an npm package. |
| **15:00–15:30**  | Short break: Snack, stretch, or meditate.                 |
| **15:30–17:30**  | Prepare and practice the demo.                            |
| **17:30–18:30**  | Dinner and relaxation.                                    |
| **18:30–20:00**  | Final adjustments to project and documentation.           |
| **20:00–21:00**  | Relaxation: Hobby, show, or light reading.                |
| **21:00–22:00**  | Wind down and sleep preparation.                          |
"""
    lines = markdown_text.split("\n")
    # Start date is today
    start_date = datetime.today()
    cal = parse_markdown_to_ics(lines, start_date)

    with open("schedule.ics", "wb") as f:
        f.write(cal.to_ical())