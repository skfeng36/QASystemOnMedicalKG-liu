#!/home/sk/anaconda3/envs/myenv/bin/python
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。如果没答上来，可联系https://liuhuanyong.github.io/。祝您身体棒棒！'
        ''' 对用户的输入语句中的词语进行分类，拆分出实体，和关系（问题要干什么）'''
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        """ 根据上一步拆分出的实体，关系，构造cypher查询语句"""
        res_sql = self.parser.parser_main(res_classify)
        
        """ 执行cypher查询语句，然后将结果拼接成定义好的回答模板返回给用户"""
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('小勇:', answer)

