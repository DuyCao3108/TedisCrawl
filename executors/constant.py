HTML_FORMAT = """<div class="block-content cms pageview-highest"><div class="summary"><div class="rich-text"><b>{}</b></div></div>{}</div>"""

SECTION_TEMPLATE = """
        Your task is to regconized the concrete sections of an craft structure for an medical post's idea; Then expand on this section.
        
        Do the following tasks:
        - Relax, dont be rush, emphasize quality over quantity.
        - Regconized the {} section of the idea structure seperated in tripe backtick below. If this section can not be found, Return an empty string like this '' and immediately stop this process.
        - Expand this section. Elaborate on it. Make sure it meets these criteria: engaging, informative, written in Vietnamese, have at least {} words.
        - Return the output in HTML format as shown below seperated by tripe forward slash

        Remember:
        - Use a wide range of structure to convey message in more engaging manner. Such as list, comparision,... But be aware, dont over-use them.
        - Use a professional, reliable, informative writing tone. 
        - Do not put any '\n' character in the output.

        output HTML format:<h2>Title for section goes here</h2><div class="rich-text"><p>&nbsp;</p><p>First paragraph for the section goes here</p><p>Second paragraph for the section goes here</p><p>Nth paragraph for the section goes here</p></div>
        
"""

AUTHORIZATION = "Basic Zm9ydGU6UFJhQyA2RGVWIG9Qd24gT3pKRyB5eU1yIG5qZkI="

WORDPRESS_URL = "https://fortepharma.vn/wp-json/wp/v2/posts"

UPLOAD_FILE_FORMATS = ['*.txt',"*.html"]

GEN_MODE_WORD_LENGTH = {
    "light": 4000,
    "medium": 6000,
    "heavy": 8000
}