from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
import pandas as pd
from executors.constant import *
import pickle

def generate_section_template(article_num_string, num_word):
    template = SECTION_TEMPLATE.format(article_num_string, num_word)
    template += """input structure: ```{idea_structure}```"""
    return template

class AritcleLengthError(Exception):
    def __init__(self, message):
        self.message = message

class Generator():

    def __init__(self, input_csv_path: str) -> ChatOpenAI:
        self.llm = ChatOpenAI(
                    model="gpt-4-turbo",
                    openai_api_key = "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",
                    temperature=0,
                    max_tokens=2000,
                    frequency_penalty=1,
                    presence_penalty=0
                )
        self.input_csv_path = input_csv_path
    
    def start_generate(self, store_path = None):
        try:
            sample_posts = self.extract_sample_posts(input_csv_path = self.input_csv_path)
            chains_param_dict = self.define_chains(llm = self.llm)
            gen_text = self.execute_chains(sample_posts, chains_param_dict)
            self.caching_gen_text(gen_text)
            gen_html, title = self.convert_to_html(gen_text)
            self.storing_output(gen_html, title, store_path)
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def extract_sample_posts(self, input_csv_path: str, mode = "medium"):
        df = pd.DataFrame(pd.read_csv(input_csv_path, index_col=0))
        max_input_length = GEN_MODE_WORD_LENGTH[mode]
        series_of_available_articles = [df.iloc[i] for i, row in df.iterrows() if len(row['article']) < max_input_length]
        if len(series_of_available_articles) < 1: 
            raise AritcleLengthError("Input articles exceed wordlength threshold")
        else:
            series_sample_article = series_of_available_articles[0]
            sample_posts = f"Title: {series_sample_article['title']};; Article: {series_sample_article['article']}"
            print("done extract_sample_posts")
            return sample_posts

    def define_chains(self, llm):
        # idea chain
        prompt0 = ChatPromptTemplate.from_template(
            """
                Do the following:
                - Read and understand the given sample posts seperated by triple backtick
                - Generate an idea for new post base on those sample posts. Make sure this idea meets these criteria: engaging, informative, written in Vietnamese.
                - Create a conceptual structure for this idea, there should be at least 3 sections and at most 5 sections. 
                
                The output format will look like:
                Title for idea: <idea>
                Title for section 1: <Title of section 1>
                <Content for section 1>
                Title for section 2: <Title of section 2>
                <Content for section 2>
                ... 
                Title for section N: <Title of section N>
                <Content for section N>
                
                sample posts: ```{sample_posts}```
            """
            )
        chain0 = LLMChain(llm = llm, prompt = prompt0, output_key = "idea_structure")
        # summmary chain
        prompt0_1 = ChatPromptTemplate.from_template(
        """
            Your task is to regconized the title of an medical post's idea; Then expand on this section.
            
            Do the following tasks:
            - Regconized the title and all the section titles of the post in the input structure, seperated in tripe backtick below.
            - Write a summary paragraph that directly answer, or address this title and all the section titles. Thinking of it as a intro to the post. Use Vietnamese, maximum 100 words. Be concise, comprehensive.
            - Look at the example given below, seperated by triple forward slash to understand the task.
            - Remember: only output the summary text
            
            input structure: ```{idea_structure}```
            example: ///
            Title: Taurine là gì? Lợi ích, tác dụng phụ và cách sử dụng
            Summary: Taurine là một loại acid amin được tìm thấy trong nhiều loại thực phẩm và thường được thêm vào nước tăng lực. Nhiều người dùng taurine như một chất bổ sung, và một số nhà nghiên cứu gọi nó là một “phân tử kỳ diệu”. Taurine đã được chứng minh có một số lợi ích sức khỏe, như giảm nguy cơ mắc bệnh và cải thiện hiệu suất thể thao.

            Title: Công dụng của thuốc Acerola – Vinmec
            Summary: Thuốc Acerola (vitamin C) xảy ra tự nhiên trong thực phẩm, chẳng hạn như trái cây họ cam quýt, cà chua, khoai tây và rau má. Vitamin C cũng rất quan trọng đối với xương và các mô liên kết, cơ bắp, mạch máu. Để hiểu rõ hơn về thuốc Acerola hãy cùng tìm hiểu thêm trong bài viết dưới đây.
            ///
        """
        )
        chain0_1 = LLMChain(llm = llm, prompt = prompt0_1, output_key = "summary")
        # extract title
        prompt0_2 = ChatPromptTemplate.from_template("""
            Do following tasks:
            - Identify the title for idea of the given title structure below seperated by triple backtick
            - Output the title
                                                     
            idea_structure: ```{idea_structure}```    
                                                                                  
        """)
        chain0_2 = LLMChain(llm = llm, prompt = prompt0_2, output_key = "title")
        # sections chain
        prompt1 = ChatPromptTemplate.from_template(generate_section_template(article_num_string = "1st", num_word = "20"))
        chain1 = LLMChain(llm = llm, prompt = prompt1, output_key = "craft1")
        
        prompt2 = ChatPromptTemplate.from_template(generate_section_template(article_num_string = "2nd", num_word = "20"))
        chain2 = LLMChain(llm = llm, prompt = prompt2, output_key = "craft2")
        
        prompt3 = ChatPromptTemplate.from_template(generate_section_template(article_num_string = "3rd", num_word = "20"))
        chain3 = LLMChain(llm = llm, prompt = prompt3, output_key = "craft3")
        
        prompt4 = ChatPromptTemplate.from_template(generate_section_template(article_num_string = "4th", num_word = "20"))
        chain4 = LLMChain(llm = llm, prompt = prompt4, output_key = "craft4")
        
        prompt5 = ChatPromptTemplate.from_template(generate_section_template(article_num_string = "5th", num_word = "20"))
        chain5 = LLMChain(llm = llm, prompt = prompt5, output_key = "craft5")
        # set chains param dict
        chains_param_dict = {
            "chains": [chain0, chain0_1, chain0_2, chain1, chain2, chain3, chain4, chain5],
            'input_variables': ["sample_posts"],
            'output_variables': ["idea_structure","summary","title","craft1","craft2","craft3","craft4","craft5"],
            'verbose': True
        }
        print("done define_chains")
        return chains_param_dict
    
    def execute_chains(self, sample_posts, chains_param_dict):
        overall_chain = SequentialChain(
            chains = chains_param_dict['chains'],
            input_variables = chains_param_dict['input_variables'],
            output_variables = chains_param_dict['output_variables'],
            verbose = chains_param_dict['verbose']
        )
        gen_text = overall_chain(sample_posts)
        print("done execute_chains")
        return gen_text
    
    def caching_gen_text(self, gen_text):
        with open("storage/cache/gen1.pkl","wb") as file:
            pickle.dump(gen_text, file)

    def convert_to_html(self, gen_text):
        title = gen_text['title']
        html_summary = gen_text['summary']

        html_detail_content = ""
        for key in list(gen_text)[4:]:
            html_detail_content += gen_text[key]

        gen_html = HTML_FORMAT.format(html_summary, html_detail_content)

        print("done convert_to_html")
        return gen_html, title

    def storing_output(self, gen_html, title, store_path):
        output_dict = {
            "title": title,
            "content": gen_html
        }
        if store_path:
            with open(store_path, "wb") as file:
                pickle.dump(output_dict, file)
                print("done storing_output")

    