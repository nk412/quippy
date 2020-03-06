```
             _                   
  __ _ _   _(_)_ __  _ __  _   _ 
 / _` | | | | | '_ \| '_ \| | | |
| (_| | |_| | | |_) | |_) | |_| |
 \__, |\__,_|_| .__/| .__/ \__, |
    |_|       |_|   |_|    |___/ 

```
**quip**<br>
*/kwip/*<br>
A quick, witty remark

Quickly fetch code snippets, text and URLs from the CLI.

## Requirements

This project makes use of [pyfzf](http://www.github.com/nk412/pyfzf) which requires [fzf](http://www.github.com/junegunn/fzf) to be installed and available on the PATH.

On a Mac, you can install it with `brew install fzf`. For more installation instructions, please see the project page.

## Installation

`pip install quippy-cli`

## Usage

Type `qp` to invoke quippy.

Keys can be added to `~/.quippy.yaml`.

On running, qp lists all the keys available through `fzf`. Selecting a key will copy its associated value to your clipboard.

## License

MIT

## Thanks

[fzf](http://www.github.com/junegunn/fzf)
