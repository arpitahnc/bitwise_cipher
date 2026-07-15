# bitwise_cipher

A simple cipher I'm building to learn how bit-level operations work in Python.

## What it does

Takes a message and scrambles it using a few steps:
1. Turn each character into binary
2. Reverse the bits
3. Rotate the bits
4. Turn it back into a character

There's also a decrypt function that undoes all of this and gets back the original message.

## How to run it

```bash
python encrypt.py
python decrypt.py
```

Run it and follow the prompts.

## Notes:

- There's no actual secret key yet, so this isn't real encryption — just bit shuffling that anyone who knows the steps could undo. Planning to add an XOR key later so it's an actual cipher.
- Some characters turn into non-printable symbols after encrypting, so copy-pasting the encrypted text between the two programs can sometimes lose characters (characters like H and A). Best to test everything in one script for now.

## Why I made this

Wanted to understand ciphers by actually building one instead of just reading about them. Learned a lot about bitwise operations and why some steps in a cipher matter more than others for actual security.
