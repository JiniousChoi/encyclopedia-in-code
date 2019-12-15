#page=get_page(url)
#get_all_links(page)
def get_next_target(page):
    start_link = page.find('href=')
    if start_link == -1:
        return None, 0, False
        
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote, True

def get_all_links(page):
    links = []
    while True:
        url, endpos, found = get_next_target(page)
        if found:
            #always the case? I don't know yet.
            url = decodeHtmlTags(url)
            url = decodeWebEncoding(url)           
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
    
def decodeHtmlTags(html):
    html = html.replace('&amp;','&')
    return html

def decodeWebEncoding(html):
    html = html.replace('%21',"!")
    html = html.replace('%27',"'")
    return html
   
