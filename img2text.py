from utils.imports import pipeline

def img2text(url):
    image_to_text = pipeline('image-to-text', model='Salesforce/blip2-opt-2.7b')
    text = image_to_text(url)[0]['generated_text']
    print(text)
    return text

url='/Users/gwenwu/Documents/photo.jpg'

if __name__=='__main__':
    img2text(url)