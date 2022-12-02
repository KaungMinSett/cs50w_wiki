from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def htmlconverter(title):
    markdowner = Markdown()
    content = util.get_entry(title)
    return markdowner.convert(content)

def entry(request, title):
    html_content = htmlconverter(title)
    return render(request, "encyclopedia/entry.html",{
        "title" : title,
        "content": html_content
    })