#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 15:04
@Author  : alexanderwu
@File    : project_manager.py
"""
from metagpt.actions import WriteDesign, WriteTasks
from metagpt.roles import Role
from metagpt.callbacks import BaseCallbackHandler


class ProjectManager(Role):
    """
    Represents a Project Manager role responsible for overseeing project execution and team efficiency.
    
    Attributes:
        name (str): Name of the project manager.
        profile (str): Role profile, default is 'Project Manager'.
        goal (str): Goal of the project manager.
        constraints (str): Constraints or limitations for the project manager.
    """
    
    def __init__(self, 
                 name: str = "Eve", 
                 profile: str = "Project Manager", 
                 goal: str = "Improve team efficiency and deliver with quality and quantity",
                 constraints: str = "",
                 callback_handler:BaseCallbackHandler=None) -> None:
        """
        Initializes the ProjectManager role with given attributes.
        
        Args:
            name (str): Name of the project manager.
            profile (str): Role profile.
            goal (str): Goal of the project manager.
            constraints (str): Constraints or limitations for the project manager.
        """
        super().__init__(name, profile, goal, constraints, callback_handler=callback_handler)
        self._init_actions([WriteTasks])
        self._watch([WriteDesign])