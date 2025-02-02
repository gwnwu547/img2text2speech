from utils.imports import PromptTemplate,LLMChain,OllamaLLM
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
    story_llm = LLMChain(
        llm=OllamaLLM(
            model='deepseek-r1:32b'
        )
        ,prompt=prompt
        ,verbose=True
    )

    story = story_llm.predict(scenario=scenario
    )
    print(story)
    return story

url= '/Users/gwenwu/Documents/photo.jpg'

if __name__=='__main__':
    scenario=img2text.img2text(url)
    generate_story(scenario)
