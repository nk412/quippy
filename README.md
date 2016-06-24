```
             _                   
  __ _ _   _(_)_ __  _ __  _   _ 
 / _` | | | | | '_ \| '_ \| | | |
| (_| | |_| | | |_) | |_) | |_| |
 \__, |\__,_|_| .__/| .__/ \__, |
    |_|       |_|   |_|    |___/ 

```
**quip**
*/kwip/*
A quick, witty remark

Quickly fetch code snippets, text and URLs from the CLI.

## Requirements

This project makes use of [pyfzf](http://www.github.com/nk412/pyfzf) which requires [fzf](http://www.github.com/junegunn/fzf) to be installed and available on the PATH.

On a Mac, you can install it with `brew install fzf`

## Usage

Type `qp` to invoke quippy.

Keys can be added to `~/.quippy.yaml`.

On running, qp lists all the keys available. If the value for the associated key begins with `http`, it will attempt to open the URL on your default browser.
For any other type of value, it will be copied into your clipboard.

## Todo

To package and make quippy installable via `pip`
