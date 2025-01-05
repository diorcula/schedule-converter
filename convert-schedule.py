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
    markdown_text = """## Monday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 05:30–06:00  | Wake up, light breakfast.                              |
| 06:00–07:00  | Optional: Short run or yoga, followed by a shower.     |
| 07:00–07:30  | Prep and leave for bus (or bike commute if weather permits). |
| 08:30–13:00  | Internship work.                                       |
| 13:00–13:30  | Lunch break (optional walk in the park).               |
| 13:30–16:30  | Internship work.                                       |
| 16:30–17:30  | Commute home and wind down.                            |
| 17:30–18:30  | Relaxation (yoga or "do nothing" time).                |
| 18:30–19:30  | Dinner.                                                |
| 19:30–21:30  | Gaming (daily 2-hour session can start here if preferred). |
| 21:30–22:30  | Social time (2–3 evenings) or gaming/relaxation.       |
| 22:30–23:00  | Wind down and sleep preparation.                       |

## Tuesday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 05:30–06:00  | Wake up, light breakfast.                              |
| 06:00–07:00  | Optional: Short run or yoga, followed by a shower.     |
| 07:00–07:30  | Prep and leave for bus (or bike commute if weather permits). |
| 08:30–13:00  | Internship work.                                       |
| 13:00–13:30  | Lunch break (optional walk in the park).               |
| 13:30–16:30  | Internship work.                                       |
| 16:30–17:30  | Commute home and wind down.                            |
| 17:30–18:30  | Relaxation (yoga or "do nothing" time).                |
| 18:30–19:30  | Dinner.                                                |
| 19:30–21:30  | Gaming (daily 2-hour session can start here if preferred). |
| 21:30–22:30  | Social time (2–3 evenings) or gaming/relaxation.       |
| 22:30–23:00  | Wind down and sleep preparation.                       |

## Wednesday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 05:30–06:00  | Wake up, light breakfast.                              |
| 06:00–07:00  | Optional: Short run or yoga, followed by a shower.     |
| 07:00–07:30  | Prep and leave for bus (or bike commute if weather permits). |
| 08:30–13:00  | Internship work.                                       |
| 13:00–13:30  | Lunch break (optional walk in the park).               |
| 13:30–16:30  | Internship work.                                       |
| 16:30–17:30  | Commute home and wind down.                            |
| 17:30–18:30  | Relaxation (yoga or "do nothing" time).                |
| 18:30–19:30  | Dinner.                                                |
| 19:30–21:30  | Gaming (daily 2-hour session can start here if preferred). |
| 21:30–22:30  | Social time (2–3 evenings) or gaming/relaxation.       |
| 22:30–23:00  | Wind down and sleep preparation.                       |

## Thursday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 05:30–06:00  | Wake up, light breakfast.                              |
| 06:00–07:00  | Optional: Short run or yoga, followed by a shower.     |
| 07:00–07:30  | Prep and leave for bus (or bike commute if weather permits). |
| 08:30–13:00  | Internship work.                                       |
| 13:00–13:30  | Lunch break (optional walk in the park).               |
| 13:30–16:30  | Internship work.                                       |
| 16:30–17:30  | Commute home and wind down.                            |
| 17:30–18:30  | Relaxation (yoga or "do nothing" time).                |
| 18:30–19:30  | Dinner.                                                |
| 19:30–21:30  | Gaming (daily 2-hour session can start here if preferred). |
| 21:30–22:30  | Social time (2–3 evenings) or gaming/relaxation.       |
| 22:30–23:00  | Wind down and sleep preparation.                       |

## Friday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 05:30–06:00  | Wake up, light breakfast.                              |
| 06:00–07:00  | Optional: Short run or yoga, followed by a shower.     |
| 07:00–07:30  | Prep and leave for bus (or bike commute if weather permits). |
| 08:30–13:00  | Internship work.                                       |
| 13:00–13:30  | Lunch break (optional walk in the park).               |
| 13:30–16:30  | Internship work.                                       |
| 16:30–17:30  | Commute home and wind down.                            |
| 17:30–18:30  | Relaxation (yoga or "do nothing" time).                |
| 18:30–19:30  | Dinner.                                                |
| 19:30–21:30  | Gaming (daily 2-hour session can start here if preferred). |
| 21:30–22:30  | Social time (2–3 evenings) or gaming/relaxation.       |
| 22:30–23:00  | Wind down and sleep preparation.                       |

## Saturday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 07:00–09:00  | Wake up, breakfast, and morning relaxation.            |
| 09:00–18:00  | Flexible block for sports (cycling, swimming, climbing, or hiking), hobbies, or social time. |
| 18:00–20:00  | Dinner with friends or family.                         |
| 20:00–00:00    | Longer gaming session or social time.                  |

## Sunday
| Time         | Activity                                               |
|--------------|--------------------------------------------------------|
| 07:30–08:00  | Wake up and breakfast.                                 |
| 08:00–09:00  | Prep and head to the running club.                     |
| 09:00–10:30  | Running club, followed by a shower.                    |
| 10:30–12:30  | Relaxation or gaming.                                  |
| 12:30–14:00  | Lunch.                                                 |
| 14:00–18:00  | Social time with friends or family.                    |
| 18:00–20:00  | Dinner.                                                |
| 20:00–22:30  | Relaxation or another long gaming session.             |
"""
    lines = markdown_text.split("\n")
    # Example: Start on Monday
    start_date = datetime(2025,1,6)
    cal = parse_markdown_to_ics(lines, start_date)

    with open("schedule.ics", "wb") as f:
        f.write(cal.to_ical())