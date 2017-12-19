# Increment File

Increment File is a utility script written in python to increment a formatted
filename with version and date. The file format is as follows:

```
<version> <name> <date mm/dd>.<extension>
```

## Examples

```
1 file name 0115.txt
13 filename 1224.doc
```

## Usage

```bash
git clone https://github.com/twh2898/inc_file-py.git
cd inc_file-py
python inc_file.pyw <path_to_file>
```

### For Windows

1. Make sure python scripts are [executable](https://docs.python.org/2/faq/windows.html)
2. Create a shortcut to `inc_file.pyw` on the Desktop
3. Drag-n-Drop a file onto the shortcut to `inc_file.pyw`

## Licence

inc_file-py uses the [MIT](LICENCE) licence
