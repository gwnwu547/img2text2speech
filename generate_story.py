from utils.imports import PromptTemplate,OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import img2text

def generate_story(scenario):
    template = '''
    你是一个很会讲故事的人，下面的context中的内容是一句英文，请你根据这句话扩展出一个有幽默感的中文的故事，字数控制在100字以内。
    context = {scenario}
    story:
    '''

    prompt = PromptTemplate(
        template=template
        ,input_variables=['scenario']
    )
    llm=OllamaLLM(model='deepseek-r1:32b')
        #,prompt=prompt
        #,verbose=False
    chain = prompt | llm | StrOutputParser()
    story_raw = chain.invoke(scenario)
    story=story_raw.split('</think>')[1].strip() # 删除deepseek-r1深度思考的部分
    print(story)
    return story

url= '/Users/gwenwu/Documents/photo.jpg'
#scenario='three women hugging on a wooden fence at sunset'

if __name__=='__main__':
    scenario=img2text.img2text(url)
    generate_story(scenario)
