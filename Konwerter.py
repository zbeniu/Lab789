import json
import argparse
import xmltodict
import yaml


def parse_args():
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('input_file', type=str, help='The input file path')
    parser.add_argument('output_file', type=str, help='The output file path')
    parser.add_argument('format', choices=['json', 'yaml', 'xml'], help='The format of the input/output files')
    return parser.parse_args()


def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def read_yaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)


def write_yaml(data, filename):
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


def read_xml(filename):
    with open(filename, 'r') as file:
        return xmltodict.parse(file.read())


def write_xml(data, filename):
    with open(filename, 'w') as file:
        file.write(xmltodict.unparse(data, pretty=True))


def main():
    args = parse_args()

    if args.format == 'json':
        data = read_json(args.input_file)
        write_json(data, args.output_file)
    elif args.format == 'yaml':
        data = read_yaml(args.input_file)
        write_yaml(data, args.output_file)
    elif args.format == 'xml':
        data = read_xml(args.input_file)
        write_xml(data, args.output_file)


if __name__ == '__main__':
    main()
