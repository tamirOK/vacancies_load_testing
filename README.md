## Description

This is a locust load testing script.
There is a single task which executes the following flow:
- creates a random vacancy
- updates the vacancy
- fetches the vacancy
- deletes the vacancy

Also, there is a background task which fetches all vacancies.

## Results

Results are in `report.html` file.
I have run it with 7 workers, 100 users and 10 users spawn rate.


## How to run

Install dependencies from `requirements.txt`,
set correct settings in `locust.conf` and run:

```
locust --config config.locust
```
