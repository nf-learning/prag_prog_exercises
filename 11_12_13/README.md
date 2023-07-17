# Exercise 11,12,13

## Exercise 11
You're rewriting an application that use to use YAML as a configuration language.
Your company has now standardized on JSON, so you have a bunch of .yaml files that
need to b turned into .json. Write a script that takes a directory and converts each
.yaml file into a corresponding .json file.

### Solution
[yaml_to_json.py](./yaml_to_json.py)
---

## Exercise 12
Your team initially chose to use camelCase names for variables, but then changed their
collective mind and switched to snake_case. Write a script that scans all the source
files for camelCase names and reports on them.

### Solution
It's more robust to use a parser since this should alter variables only and not 
just any camelCase text, method names etc. Going with the less robust script which
is what the exercise asks for.
[camel_case_finder.py](./camel_case_finder.py)

---

## Exercise 13
Following on from the previous exercise, add the ability to change those variable
names automatically in one or more files. Remember to keep a backup of the originals
in case something goes horribly, horribly wrong.
### Solution
[camel_case_finder.py](./camel_case_finder.py)

