# schedule-converter

## Description

This project contains a script that converts a schedule written in markdown format into an ICS (iCalendar) file. This can be useful for importing schedules into calendar applications like Google Calendar, Outlook, etc.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
   ```sh
   pip install icalendar
   ```
3. Modify the `markdown_text` variable in `convert-schedule.py` to match your schedule.
4. Run the script:
   ```sh
   python convert-schedule.py
   ```
5. The script will generate a file named `schedule.ics` in the same directory.

## Example

The script currently includes an example schedule for Saturday and Sunday. You can modify this example to fit your needs.

## Dependencies

- Python 3.x
- icalendar

## License

This project is licensed under the MIT License.
