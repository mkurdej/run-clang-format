# run-clang-format
Script to run clang-format on all files in a directory

## Usage

To run clang-format over all files in `source_dir` directory, just run:

```
python run-clang-format.py -d source_dir
```

If you want to specify the style for formatting (by default `file` style is used), then execute:
```
python run-clang-format.py -style FILE -d source_dir
```

You can specify the number of threads that will be used to reformat the code with `-j` option (when unspecified, the CPU count will be used):

```
python run-clang-format.py -d source_dir -j 16
```

You may specify multiple directories to run `clang-format` over using multiple `-d` options:

```
python run-clang-format.py -d source_dir1 -d source_dir2
```
