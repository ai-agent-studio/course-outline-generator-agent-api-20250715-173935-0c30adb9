#!/usr/bin/env python3
"""
Generated agent: Course Outline Generator
Factory function to create the agent with runtime context and enhanced memory.
"""

from agno.agent import Agent
from agno.knowledge.base import AgentKnowledge
from dotenv import load_dotenv
from loguru import logger
from pathlib import Path
import os

from typing import Optional
from textwrap import dedent

class MemoryEnabledCourse_Outline_Generator:
    """Course Outline Generator with enhanced conversation memory capabilities"""
    
    def __init__(self, user_id: str, session_id: str, debug_mode: bool = False):
        self.user_id = user_id
        self.session_id = session_id
        self.debug_mode = debug_mode
        self.agent = None
        self.conversation_history = []
        self.last_query_context = ""
        self.setup_agent()
        
    def setup_agent(self):
        """Initialize the agent with memory capabilities"""
        
        model = OpenAIChat(id="llama-3.3-70b-versatile", api_key=os.getenv("LLM_PROXY_API_KEY"), base_url=os.getenv("LLM_BASE_URL"))
        tools = None
        knowledge = {"type": "pdf_url", "urls": ["https://files.4gd.ai/minio/pesuacademy-data/Courses_Bank%2FUE22CS341A%2FUE22CS341A_CourseContent%2FSoftware_Engineering_Course_Outline.pdf"], "vector_db": {"name": "pgvector", "db_url": os.getenv("DATABASE_URL"), "table_name": "pdf_url_vectors", "search_type": "hybrid"}}
        
        # Create agent with memory and runtime parameters
        self.agent = Agent(
            user_id=self.user_id,
            session_id=self.session_id,
            debug_mode=self.debug_mode,
            model=model,
            tools=tools,
            knowledge=knowledge,
            name="Course Outline Generator",
            description="""This agent generates structured, pedagogically-aligned course outlines 
""",
            goal="""To automatically generate a high-quality, structured course outline from faculty-uploaded content 
""",
            instructions="""  - Process all uploaded course content (PDFs, slides, reference books) in a systematic, structured manner.
  - Extract only relevant academic material and semantically organize it into a complete course outline.
  - Adhere strictly to the following output format and structure — do not skip any section:
  
    1️⃣ **Course Details**  
    - Course Title: [Extract from material or infer]  
    - Course Code: [If available]  
    - Semester & Year: [Infer or leave placeholder]  
    - Credits: [If specified]  
    - Contact Hours (L-T-P-S): [Format as 3-0-2-4 or similar]  
    - Prerequisites: [Mention if listed; else write “None”]

    2️⃣ **Course Description**  
    - Write a short paragraph (3–5 sentences) summarizing the scope and intent of the course.

    3️⃣ **Course Objectives**  
    - List 3 to 5 concise academic goals of the course (bullet points).

    4️⃣ **Course Outcomes**  
    - List 4 to 6 measurable outcomes showing what students will be able to do by the end of the course.

    5️⃣ **Course Content / Syllabus**  
    - Divide the content into exactly 4 units.  
    - For each unit, provide:  
      - **Unit Number and Title**  
      - Sub-topics covered (at least 4–5 points per unit)  
      - Number of Hours allocated to the unit

    6️⃣ **Teaching Methodology**  
    - Describe instructional approaches used: lectures, labs, case studies, projects, etc.

    7️⃣ **Assessment Scheme**  
    - Explain how the student will be assessed:  
      - Continuous Internal Evaluation (CIE): [e.g., 40%]  
      - End Semester Exam (ESE): [e.g., 60%]  
      - Mention any group projects or presentations if relevant

    8️⃣ **Reference Materials**  
    - List the primary textbook(s) and any supplementary reference books.

    9️⃣ **Mapping with Program Outcomes (POs) & Program Specific Outcomes (PSOs)**  
    - Include a simple mapping (table or list) showing alignment between Course Outcomes and POs/PSOs.

    🔟 **Additional Information**  
    - Add notes on lab components, tools used, optional certifications, industry case studies, or fieldwork.

  - Ensure the tone is formal, academic, and neutral — avoid opinions, casual language, or unverifiable claims.
  - Avoid hallucinations or assumptions not grounded in the provided materials.
  - Provide inline debug logs with section titles during processing (e.g., “✅ Parsed Unit 2”, “🔍 Extracting course outcomes…”).
""",
            show_tool_calls=True,
            markdown=True,
            role="Course Outline Generation Agent",
            search_knowledge=True,
            agent_id="2fb301c9-6969-426f-87fd-1d12df89adfb",
        )
    
    def ask(self, question: str) -> str:
        """Ask a question with memory context"""
        
        # Enhance question with context for follow-up queries
        enhanced_question = question
        follow_up_indicators = ["those", "that", "these", "same", "previous", "earlier", "them"]
        if any(indicator in question.lower() for indicator in follow_up_indicators):
            if self.last_query_context:
                enhanced_question = f"[CONTEXT: {self.last_query_context}]\n\nUser question: {question}"
        
        # Get response from agent
        response = self.agent.run(enhanced_question)
        
        # Extract content
        if hasattr(response, 'content'):
            agent_response = response.content
        else:
            agent_response = str(response)
        
        # Update context for next query
        self.update_context(question, agent_response)
        return agent_response
    
    def update_context(self, question: str, response: str):
        """Update context based on the latest query"""
        context_parts = []
        question_lower = question.lower()
        
        # Add context based on question content
        if "department" in question_lower:
            if "distribution" in question_lower or "count" in question_lower:
                context_parts.append("Previously analyzed department distribution")
            elif "satisfaction" in question_lower:
                context_parts.append("Previously analyzed job satisfaction by department")
        
        # Add more context patterns as needed
        if "employee" in question_lower:
            context_parts.append("Previously discussed employee data")
        
        self.last_query_context = ". ".join(context_parts)

def course_outline_generator_agent(
    user_id: str,
    session_id: str,
    model_id: str = "gpt-4o",
    debug_mode: bool = False,
) -> MemoryEnabledCourse_Outline_Generator:
    """
    Factory function to create the agent with runtime context and enhanced memory.
    """
    return MemoryEnabledCourse_Outline_Generator(user_id=user_id, session_id=session_id, debug_mode=debug_mode)