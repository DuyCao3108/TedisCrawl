class user_input
    function: GET
        - keyword
        - max_article
        - from_websites
    output:
        void
        execute process_user_input


class process_user_input
    for website in from_websites:
        crawl_data_from_website()



class crawl_data_from_website()
    input:
        