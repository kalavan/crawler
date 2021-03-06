import mechanize
import re


def loop_through_olx(start_url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.open(start_url)
    have_next_link = True
    links_found = []

    while have_next_link:
        try:
            print "Looking for links on page %s" % browser.geturl()
            links = [link.url for link in browser.links(url_regex=re.compile(".*/oferta/.*"))]
            links_found = list(set(links_found + links))
            print "Trying to follow next link"
            browser.follow_link(text_regex=re.compile("^nast\xc4\x99pna"))
        except mechanize.LinkNotFoundError:
            have_next_link = False
            print "No more links to follow."
    return links_found

# links = loop_through_olx("https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?page=499")
# print "Found %s links. Links are:" % len(links)
# for link in links:
#     print link

# vim: expandtab:ts=4:sw=4:sts=4
