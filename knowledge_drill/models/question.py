from typing import List, Dict, Tuple
from pydantic import BaseModel

class MultipleChoiceQuestion(BaseModel):
    question: str
    choices: List[str]
    correct_answer_index: int

class TrueOrFalseQuestion(BaseModel):
    statement: str
    answer: bool

class FillInTheBlanksQuestion(BaseModel):
    words: List[str]  
    choices: List[List[str]]
    blanks: List[Tuple[int, str]] 

class MatchingQuestion(BaseModel):
    list_one: List[str]
    list_two: List[str]
    correct_matches: Dict[str, str] 

class ShortAnswerQuestion(BaseModel):
    question: str
    correct_answer: str

question_types = [MultipleChoiceQuestion, TrueOrFalseQuestion, MatchingQuestion, ShortAnswerQuestion]

special_instructions = {
    MultipleChoiceQuestion: '',

    TrueOrFalseQuestion:'',

    MatchingQuestion:'',

    ShortAnswerQuestion:''
}