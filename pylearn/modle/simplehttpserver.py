# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/10/14 18:57


"""Simple HTTP Server With Upload.

This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.

see: https://gist.github.com/UniIsland/3346170
"""

__version__ = "0.1"
__all__ = ["SimpleHTTPRequestHandler"]

import os
import posixpath
import http.server
import urllib.request, urllib.parse, urllib.error
import cgi
import shutil
import mimetypes
import re
import sys
import html
import getopt


from io import BytesIO
from http.server import HTTPServer, BaseHTTPRequestHandler


ip = 'localhost'
port = 8085
dir = ""

def tran_code(str):
    print(str)
    if len(str.split(".")) != 2:
        print("2222")
        return str
    if str.split(".")[0].find('&#') == -1:
        print("333")
        return str
    text = str.split(".")[0].replace('&#', '')
    print(text)
    text = [i for i in text.split(';') if i]
    print(text)

    string = ""
    flag = '\\u'
    for it in text:
        if it.isdigit() and len(it)== 5:
            print("-------")
            print(it)
            ss = hex(int(it))
            print(type(ss))
            if ss.find("0x") != -1:
                ss = ss[ss.find("0x")+2:]
            temp =  flag + format(ss, '0>4s')
            temp = temp.encode('utf-8').decode('unicode-escape')
            print(temp)
            string += temp
        else:
            string += it

    string += "."
    string += str.split(".")[1]
    return string

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP request handler with GET/HEAD/POST commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method. And can reveive file uploaded
    by client.

    The GET/HEAD/POST requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    server_version = "SimpleHTTPWithUpload/" + __version__

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.send_head()
        if f:
            f.close()

    def do_POST(self):
        """Serve a POST request."""
        r, info = self.deal_post_data()
        print((r, info, "by: ", self.client_address))
        f = BytesIO()
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b"<html>\n<title>Upload Result Page</title>\n")
        f.write(b''' <head>\n <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head>\n''')

        f.write(b"<body>\n<h2>Upload Result Page</h2>\n")
        f.write(b"<hr>\n")
        if r:
            f.write(b"<strong>Success:</strong>")
        else:
            f.write(b"<strong>Failed:</strong>")
        f.write(info.encode())
        f.write(("<br><a href=\"%s\">back</a>" % self.headers['referer']).encode())
        f.write(b"<hr><small>Powerd By: bones7456, check new version at ")
        f.write(b"<a href=\"http://li2z.cn/?s=SimpleHTTPServerWithUpload\">")
        f.write(b"here</a>.</small></body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def deal_post_data(self):
        content_type = self.headers['content-type']
        print(f'content_type{content_type}')
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")
        boundary = content_type.split("=")[1].encode()
        remainbytes = int(self.headers['content-length'])
        print(f"remainbytes {remainbytes}")
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content NOT begin with boundary")
        line = self.rfile.readline()
        remainbytes -= len(line)

        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode("GBK","ignore"))
        if not fn:
            return (False, "Can't find out file name...")
        path = self.translate_path(self.path)

        print(f"fn[0] {fn[0]}")

        print(f"fn[0] {tran_code(fn[0])}")
        fname = tran_code(fn[0])
        fn = os.path.join(path, fname)

        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")

        preline = self.rfile.readline()
        remainbytes -= len(preline)
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "File '%s' upload success!" % fn)
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpect Ends of data.")

    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
        print(f"selft.path {self.path}")
        path = self.translate_path(self.path)
        print(f"send_head start {path}")

        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                print(f"index {index}")
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        print(f"ctype {ctype}")
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        print(f"fs {fs}")
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        f = BytesIO()
        displaypath = html.escape(urllib.parse.unquote(self.path))
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(("<html>\n<title>Directory listing for %s</title>\n" % displaypath).encode())
        f.write(("<body>\n<h2>Directory listing for %s</h2>\n" % displaypath).encode())
        f.write(b"<hr>\n")
        f.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
        f.write(b"<input name=\"file\" type=\"file\"/>")
        f.write(b"<input type=\"submit\" value=\"upload\"/></form>\n")
        f.write(b"<hr>\n<ul>\n")
        for name in list:
            fullname = os.path.join(path, name)
            print(f"fullname {fullname}")
            displayname = linkname = name

            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
                print(f"displayname {displayname}")
                print(f"linkname {linkname}")
            if os.path.islink(fullname):
                displayname = name + "@"
                print(f"displayname {displayname}")
                # Note: a link to a directory displays with @ and links with /
            f.write(('<li><a href="%s">%s</a>\n'
                     % (urllib.parse.quote(linkname), displayname)).encode("GBK"))
        f.write(b"</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        # abandon query parameters
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = posixpath.normpath(urllib.parse.unquote(path))
        print(f"path {path}")
        words = path.split('/')
        words = [_f for _f in words if _f]
        global  dir
        path = ""
        if os.path.isdir(dir):
            path =dir
        else:
            path = os.getcwd()


        print(f"path {path}")
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path

    def copyfile(self, source, outputfile):
        """Copy all data between two file objects.

        The SOURCE argument is a file object open for reading
        (or anything with a read() method) and the DESTINATION
        argument is a file object open for writing (or
        anything with a write() method).

        The only reason for overriding this would be to change
        the block size or perhaps to replace newlines by CRLF
        -- note however that this the default server uses this
        to copy binary data as well.

        """
        
        shutil.copyfileobj(source, outputfile)

    def guess_type(self, path):
        """Guess the type of a file.

        Argument is a PATH (a filename).

        Return value is a string of the form type/subtype,
        usable for a MIME Content-type header.

        The default implementation looks the file's extension
        up in the table self.extensions_map, using application/octet-stream
        as a default; however it would be permissible (if
        slow) to look inside the data to make a better guess.

        """

        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init()  # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream',  # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
    })





def test(ip,port,dir):
    HandlerClass = SimpleHTTPRequestHandler

    host =(ip,int(port))
    print(f"{ip}:{port}_{dir}")
    server = HTTPServer(host, HandlerClass)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()


def getargs(argv):

    global  port
    global  ip
    global  dir

    try:
        opts, args = getopt.getopt(argv, "hi:p:d:", ["ip=", "port=" ,"dir="])
    except getopt.GetoptError:
        print('httpfile.py -i <ip>  -p <port> -d <dir>  -h help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('httpfile.py -i <ip>  -p <port> -d <dir>  -h help')
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-d", "--dir"):
            dir = arg
    print( f"{ip}_{port}_{dir}")

if __name__ == '__main__':
    getargs(sys.argv[1:])
    test(ip,port ,dir)
