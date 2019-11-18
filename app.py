from flask import Flask, request
import difflib

app = Flask(__name__)

def check_diff(html1, html2):
    lines1 = get_lines(html1)
    lines2 = get_lines(html2)
    d = difflib.Differ()
    diif = difflib.HtmlDiff(wrapcolumn=80).make_table(lines1,lines2,context=True,numlines=0)
    return diif

def get_lines(source):
    text = "".join([l.strip() for l in source.splitlines()])
    return [l for l in text.replace("><", ">><<").split("><")]

line1 = "<html><a><b>c</b></a></html>"

line2 = """<html>
<a>
<b>c</b>
</a>
</html>"""

line3 = """
<html>
    <a href="#">
        <b>c</b>
    </a>
</html>
"""

# print(get_lines(line1))
# print(get_lines(line2))
# print(get_lines(line3))

@app.route('/')
def index():
    return check_diff(line1, line3)

if __name__ == '__main__':
    # import inspect
    # print([m for m in inspect.getmembers(request) if not m[0].startswith("_")])
    # print([m for m in inspect.getmembers(request)])
    # print(request.host)
    app.run(debug=True)