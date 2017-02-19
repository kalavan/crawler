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
            links = find_links(browser.links())
            yield links
            print "Trying to follow next link"
            browser.follow_link(text_regex=re.compile("^nast\xc4\x99pna"))
        except mechanize.LinkNotFoundError:
            have_next_link = False
            print "No more links to follow."


def find_links(link_list):
    links_found = []
    for link in link_list:
        for attr in link.attrs:
            if attr[0] == 'class':
                if "marginright5 link linkWithHash detailsLink" in attr[1]:
                    links_found.append(link.url)
    return links_found


# links = loop_through_olx("https://www.olx.pl/nieruchomosci/mieszkania/?page=499")
# links = loop_through_olx("https://www.olx.pl/nieruchomosci/mieszkania/")
# links = loop_through_olx("https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?page=499")
# print "Found %s links. Links are:" % len(links)
# for link in links:
#     print link

for links in loop_through_olx("https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?page=499"):
    print "This time I found %s links" % len(links)
    for link in links:
        print link

# vim: expandtab:ts=4:sw=4:sts=4
