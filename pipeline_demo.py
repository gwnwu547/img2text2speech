
from transformers import pipeline


# import torch
#
# torch.backends.mps.is_available()
#

# [{'label': 'POSITIVE', 'score': 0.9998782873153687}]

classifier=pipeline('sentiment-analysis')
res=classifier('Today is a nice day!')
print(res)

# 扩展text
generator=pipeline(task='text-generation',model='distilgpt2')
res=generator(text_inputs='i love this course,we will knowledge about huggingface'
              ,max_length=30
              ,num_return_sequences=2)
print(res)

# 零样本分类
classifier = pipeline('zero-shot-classification')
res = classifier(
    'this is a course about python list comprehension'
    ,candidate_labels=['education','politics','business']
)
print(res)



