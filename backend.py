001 from fastapi import FastAPI
002 from fastapi.middleware.cors import CORSMiddleware
003 from pydantic import BaseModel
004
005 app = FastAPI(title=&quot;EduGenie AI Educational Assistant&quot;)
006
007 app.add_middleware(
008 CORSMiddleware,
009 allow_origins=[&quot;*&quot;],
010 allow_credentials=True,
011 allow_methods=[&quot;*&quot;],
012 allow_headers=[&quot;*&quot;],
013 )
014
015 class AskRequest(BaseModel):
016 question: str
017
018 class QuizRequest(BaseModel):
019 topic: str
020
021 class PathRequest(BaseModel):
022 topic: str
023
024 def answer_question(question: str) -&gt; str:
025 q = question.lower()
026 if &quot;largest ocean&quot; in q:
027 return &quot;The Pacific Ocean is the largest ocean on Earth.&quot;
028 if &quot;pythagoras&quot; in q:
029 return &quot;The Pythagorean Theorem states that in a right triangle, a² + b² = c².&quot;
030 if &quot;sql&quot; in q:
031 return &quot;SQL is a language used to store, retrieve, and manage data in relational databases.&quot;
032 return &quot;EduGenie: Please ask a specific academic question. I can explain concepts in simple
language.&quot;
033
034 def generate_quiz(topic: str):
035 t = topic.lower()
036 if &quot;pythagoras&quot; in t:
037 return [
038 {&quot;question&quot;: &quot;What is the Pythagorean Theorem?&quot;, &quot;answer&quot;: &quot;a² + b² = c²&quot;},
039 {&quot;question&quot;: &quot;Which side is c?&quot;, &quot;answer&quot;: &quot;The hypotenuse&quot;},
040 {&quot;question&quot;: &quot;When is the theorem used?&quot;, &quot;answer&quot;: &quot;In a right-angled triangle&quot;},
041 {&quot;question&quot;: &quot;If a=3 and b=4, what is c?&quot;, &quot;answer&quot;: &quot;5&quot;},
042 {&quot;question&quot;: &quot;What is the longest side of a right triangle?&quot;, &quot;answer&quot;: &quot;The hypotenuse&quot;},
043 ]
044 return [
045 {&quot;question&quot;: f&quot;What is {topic}?&quot;, &quot;answer&quot;: f&quot;{topic} is an important learning topic.&quot;},
046 {&quot;question&quot;: f&quot;Why should we learn {topic}?&quot;, &quot;answer&quot;: &quot;It helps build academic understanding
and practical skills.&quot;},
047 {&quot;question&quot;: f&quot;Give one example of {topic}.&quot;, &quot;answer&quot;: &quot;A practical example related to the
topic.&quot;},
048 ]
049
050 def learning_path(topic: str):
051 if topic.lower() == &quot;sql&quot;:
052 return {
053 &quot;topic&quot;: &quot;SQL&quot;,
054 &quot;timeline&quot;: &quot;4 weeks&quot;,
055 &quot;levels&quot;: [
056 {&quot;level&quot;: &quot;Beginner&quot;, &quot;topics&quot;: [&quot;Database basics&quot;, &quot;Tables and records&quot;, &quot;SELECT&quot;,
&quot;WHERE&quot;, &quot;ORDER BY&quot;]},
057 {&quot;level&quot;: &quot;Intermediate&quot;, &quot;topics&quot;: [&quot;INSERT, UPDATE, DELETE&quot;, &quot;JOINs&quot;, &quot;GROUP BY&quot;,
&quot;Aggregate functions&quot;, &quot;Subqueries&quot;]},

058 {&quot;level&quot;: &quot;Advanced&quot;, &quot;topics&quot;: [&quot;Indexes&quot;, &quot;Views&quot;, &quot;Transactions&quot;, &quot;Normalization&quot;,
&quot;Query optimization&quot;]},
059 ],
060 &quot;suggestions&quot;: [
061 &quot;Practice 5 SQL queries every day.&quot;,
062 &quot;Build a small student database project.&quot;,
063 &quot;Solve beginner-to-advanced SQL problems.&quot;
064 ]
065 }
066 return {
067 &quot;topic&quot;: topic,
068 &quot;timeline&quot;: &quot;4 weeks&quot;,
069 &quot;levels&quot;: [
070 {&quot;level&quot;: &quot;Beginner&quot;, &quot;topics&quot;: [&quot;Basic concepts&quot;, &quot;Terminology&quot;, &quot;Simple examples&quot;]},
071 {&quot;level&quot;: &quot;Intermediate&quot;, &quot;topics&quot;: [&quot;Core techniques&quot;, &quot;Practice exercises&quot;, &quot;Mini
project&quot;]},
072 {&quot;level&quot;: &quot;Advanced&quot;, &quot;topics&quot;: [&quot;Advanced concepts&quot;, &quot;Optimization&quot;, &quot;Final project&quot;]},
073 ],
074 &quot;suggestions&quot;: [&quot;Study 30 minutes daily.&quot;, &quot;Practice with examples.&quot;, &quot;Build a mini project.&quot;]
075 }
076
077 @app.get(&quot;/&quot;)
078 def home():
079 return {&quot;message&quot;: &quot;EduGenie is running&quot;}
080
081 @app.post(&quot;/ask&quot;)
082 def ask(request: AskRequest):
083 return {&quot;answer&quot;: answer_question(request.question)}
084
085 @app.post(&quot;/quiz&quot;)
086 def quiz(request: QuizRequest):
087 return {&quot;topic&quot;: request.topic, &quot;quiz&quot;: generate_quiz(request.topic)}
088
089 @app.post(&quot;/learning-path&quot;)
090 def path(request: PathRequest):
091 return learning_path(request.topic)