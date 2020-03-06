from pyfzf.pyfzf import FzfPrompt
import pyperclip
import os
import yaml
import sys

def main():
    project_dir = os.path.dirname(os.path.realpath(__file__))
    snippet_file = os.path.join(os.getenv("HOME"), ".quippy.yaml")
    if not os.path.isfile(snippet_file):
        with open(snippet_file, 'a') as f:
            f.write('"I\'m a sample key": "and I\'m a sample value"')

    snippets = yaml.load(open(snippet_file), Loader=yaml.FullLoader)
    if not snippets:
        raise SystemError("No keys found in {0}".format(snippet_file))

    fzf = FzfPrompt()

    key = fzf.prompt(snippets.keys())
    pyperclip.copy(snippets.get(key[0]))


if __name__ == '__main__':
    main()
