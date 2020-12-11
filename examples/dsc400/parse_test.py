import os
from pathlib import Path
import tomlkit
import yaml
import json
import re


def main():
    current_dir = Path(Path(Path(__file__).parent).absolute())
    course_yaml = current_dir.joinpath('course.yaml')
    course_toml = current_dir.joinpath('course.toml')

    with open(course_yaml) as f:
        yaml_data = yaml.load(f, Loader=yaml.CLoader)

    # topics = yaml_data['topics']
    # for topic in topics:
    #     print(topic.split('::'))
    print(json.dumps(yaml_data, indent=2))

    # with open(course_toml) as f:
    #     toml_data = tomlkit.loads(f.read())
    #
    # print(json.dumps(toml_data, indent=2))


if __name__ == '__main__':
    main()
