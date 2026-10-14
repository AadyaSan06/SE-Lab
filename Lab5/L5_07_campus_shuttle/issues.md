# Static Code Analysis — Issues Found

| ID | Severity | Issue | Location in Original code | Fix |
|---|---|---|---|---|
| ISS-01 | High | Invalid passenger counts, including negative numbers and strings, are accepted. | `add_trip_log()`; lines 12–14 | Validate route IDs and require non-negative integer passenger counts. |
| ISS-02 | High | The program crashes when calculating the average of an empty route or a route that has been removed. | `average_load()`; lines 20–22 and `main()` | Handle empty routes and check that a route exists before accessing it. |
| ISS-03 | Medium | A bare exception silently hides errors during underused-route detection. | `underused_routes()`; lines 25–31 | Handle empty trips explicitly rather than catching every exception. |
| ISS-04 | Medium | A mutable default list is shared between calls to `add_trip_log()`. | `add_trip_log()`; line 11 | Use `None` as the default and create a new list when needed. |
| ISS-05 | Medium | Files are opened without context managers or explicit encoding. | `sync_fleet_data()`; lines 37–43 | Use `Path.write_text()` with UTF-8 encoding. |
| ISS-06 | Medium | The fleet dictionary is unnecessarily reassigned after the file is read back. | `sync_fleet_data()`; lines 38–43 | Save the data without reloading and reassigning the global dictionary. |
| ISS-07 | Low | `assignDriver()` does not follow the snake_case naming convention and ignores its route argument. | `assignDriver()`; lines 33–35 | Rename it to `assign_driver()` and validate the route. |
| ISS-08 | Low | The module and functions lack documentation strings, and some formatting violates Python conventions. | Throughout the file | Add docstrings and format the code consistently. |
| ISS-09 | Low | The program starts running whenever the module is imported. | Final line | Use an `if __name__ == "__main__":` guard. |

## Baseline Results

- Pylint score: 6.25/10.
- Bandit: two low-severity findings.
- Flake8: formatting violations and a bare-exception violation.
- Runtime: `KeyError: 'R3'` after the route is removed.

## Fix Verification

The issues will be verified by rerunning the program, testing invalid inputs and empty routes, validating the saved JSON, and rerunning Pylint, Bandit and Flake8.
