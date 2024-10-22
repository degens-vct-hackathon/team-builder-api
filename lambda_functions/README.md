# Update Lambda Functions

This submodule allows you to work on Lambda Functions locally.

## Usage

```sh
python lambda_functions/update_lambda_functions.py
```

Follow CLI prompts to download and upload Lambda Functions. You can use `-y` during the options menu to skip confirmation.

The functions will be stored locally at `lambda_functions/functions/<function-name>`.

## Limitations

There is no diff tool set up so you cannot fetch new data. If you want the latest data from AWS, delete the local copy and pull a new copy.

Alternatively you can work solely through Git.
