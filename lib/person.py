#!/usr/bin/env python3

#Define a name property for your Person class. The name must be of type str and between 1 and 25 characters. The name should be converted to title caseLinks to an external site. before it is saved. Your __init__ method should receive a default argument for name.
#If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."
#Define a job property for your Person class. Your __init__ method should receive a default argument for job.
#If the job is invalid, the setter method should print() "Job must be in list of approved jobs." The job must be in the following list of jobs:

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing",
]
approved_jobs = ["Admin", "Customer Service", "Human Resources", "IT", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]


class Person:
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value.title()  # Convert to title case

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in approved_jobs:
            print("Job must be in list of approved jobs.")
        self._job = value
