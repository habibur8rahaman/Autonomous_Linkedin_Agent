import post_links, post_extraction


links = post_links.links()

for link in links:
    print(link)
    post_extraction.extracted_post(link)
