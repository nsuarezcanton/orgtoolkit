# orgtoolkit

## Getting Started

1. Clone the repo.
2. Access the root directory of the repo with `cd datadog-mwl-report`.
3. Make a virtual environment with `python -m venv <name_of_virtual_environment>` (e.g. `python -m venv venv`)
4. Source the newly created virtual environment with `. <name_of_virtual_environment>/bin/activate` (e.g. `. venv/bin/activate`).
5. Install dependencies with `pip install -r requirements.txt`.
6. Install the cli with `pip install --editable .`. You can also do `pip install .` but the changes you make won't automatically reflected at runtime — you'd need to do the install again.
7. To use the tool, run `orgtoolkit mwl-report --limit 10 --price 1.25`. Keep in mind that `--limit` and `--price` allow you to customize the number of top metrics to analyze and the price per 100 Custom Metrics respectively.

## Noteworthy

Make sure the following environment variables are set:

```bash
export DD_API_KEY="<DD_API_KEY>"
export DD_APP_KEY="<DD_APP_KEY>"
export DD_SITE="<DD_SITE>"
```
