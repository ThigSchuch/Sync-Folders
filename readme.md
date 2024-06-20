# Sync-Folders

Sync-Folders is a simple tool to synchronize two folders.\
You can use it through CLI or using a json configuration file.\
The project doesn't use any external library but the built-in Python libraries.

## Features
- Synchronize two folders
- Define interval between synchronizations
- Log each synchronization operation
- Define log location
- Delete files from replica folder if not present in source folder
- Recursive folder synchronization

## Used Libraries
- abc
- argparse
- datetime
- hashlib
- json
- os
- pathlib
- shutil
- time

## How to use

### Clone the repository

```bash
git clone https://github.com/ThigSchuch/Sync-Folders.git
cd Sync-Folders
```


### CLI

You can run the program with some arguments.

__--source__ - Source folder path.\
__--replica__ - Replica folder path.\
__--interval (optional)__ - Interval between synchronizations in seconds. Default is 60 seconds.\
__--log (optional)__ - Log file location. Default is sync.log at root project folder.

```bash
python3 main.py --source /path/to/source --replica /path/to/replica --interval 10 --log /path/to/log
```


### Configuration File
On the first run, the program will ask some questions and create a configuration file named `config.json` and use it to run in the next times when no arguments are passed.

```bash
python3 main.py
```

__config.json__ example:

```json
{
    "source": "/path/to/source",
    "replica": "/path/to/replica",
    "interval": 60,
    "log": "sync.log"
}
```

## Tests

If you want to run the tests, you need to install the `pytest` library and `pytest-mock`.

```bash
pip install pytest pytest-mock
```

Then, you can run the tests.

```bash
pytest
```

## CAREFUL WITH WHICH FOLDERS YOU CHOOSE TO SYNC
_I'm not responsible for any data loss._

## License

```
MIT License

Copyright (c) [2024] [ThigSchuch]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
