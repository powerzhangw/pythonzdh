


def search_js( value):
    jsvalue = "document.getElementById('dateObj').value='%s'" % (value)
    print(jsvalue)

print(search_js("20190105"))