from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .models import Course
from crewai_tools import SerperDevTool, WebsiteSearchTool

serper_dev_tool = SerperDevTool()
web_dev_tool = WebsiteSearchTool()


@CrewBase
class Cleeroute():
    """Cleeroute crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    ### Buildings agents
    @agent
    def Course_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['Course_planner'],
            tools=[serper_dev_tool,web_dev_tool],
            verbose=True
        )

    @agent
    def Content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['Content_writer'],
            tools=[serper_dev_tool,web_dev_tool],
            verbose=True
        )
    

    @agent
    def quiz_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_builder'],
            tools=[serper_dev_tool,web_dev_tool],
            verbose=True
        )

    @agent
    def project_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['project_builder'],
            tools=[serper_dev_tool,web_dev_tool],
            verbose=True
        )
    
    @agent
    def Course_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['Course_compiler'],
            tools=[serper_dev_tool,web_dev_tool],
            verbose=True
        )

    ### Building task
    @task
    def Course_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['Course_planner_task'],
        )

    @task
    def content_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_writer_task'],
        )
    
    @task
    def Quiz_builder_task(self) -> Task:
        return Task(
            config=self.tasks_config['Quiz_builder_task'],
        )
    
    @task
    def project_builder_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_builder_task'],
        )
    
    @task
    def Course_compiler_task(self) -> Task:
        return Task(
            config=self.tasks_config['Course_compiler_task'],
            output_pydantic= Course
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Cleeroute crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )