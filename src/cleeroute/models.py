from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class CourseInput(BaseModel):
    topic: str
    objective: str
    prerequisites: str

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

class Project(BaseModel):
    title: str
    description: str
    objectives: List[str]
    deliverables: List[str]
    evaluation_criteria: Optional[List[str]] = None

class Subsection(BaseModel):
    title: str
    description: str

class Section(BaseModel):
    title: str
    subsections: List[Subsection]
    quiz: Optional[List[QuizQuestion]] = []
    project: Optional[Project] = None

class Course(BaseModel):
    title: str
    introduction: Optional[str] = None
    sections: List[Section]

class Compagny(BaseModel):
    name: List[str]